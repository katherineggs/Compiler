import abstracts.Node as Nodo
import abstracts.Program as Program
import parser1.ParseMethods as ParseMethods
import re
from anytree import RenderTree

class Parser:
    def parser(self, tokens, debug):
        # program es el lugar peincipal en donde todo se almacena
        mainParser = Program.Program(['', '', '', '', '', ''])
        listaErrores = []
        lenTokens = len(tokens)
        ya = False 

        if lenTokens < 4 : # no hay nada 
            print("No hay suficientes tokens")
        else:
            if tokens[0].tipoSimbolo.regEx != 'class' :
                listaErrores.append("Parse error, Falta - class token")
            
            if tokens[1].tipoSimbolo.regEx != 'Program' :
                listaErrores.append("Parse error, Falta - regEx of class token")

            if '{' != tokens[2].value :
                listaErrores.append("Parse error, Falta - first { token")

            if '}' != tokens[lenTokens-1].value :
                listaErrores.append("Parse error, Falta - last closing } token")
            
            # si empieza bien
            if tokens[0].tipoSimbolo.regEx == 'class' and tokens[1].tipoSimbolo.regEx == 'Program' and '{' in tokens[2].tipoSimbolo.regEx and '}' in tokens[lenTokens-1].tipoSimbolo.regEx :
                mainParser.lista[0] = Nodo.Nodo(tokens[0], tokens[0].tipoSimbolo.regEx, []) # class
                mainParser.lista[1] = Nodo.Nodo(tokens[1], tokens[1].tipoSimbolo.regEx, [])   # program
                mainParser.lista[2] = Nodo.Nodo(tokens[2], tokens[2].value, [])   # {
                # mainParser.lista[ 3 y 4 ] quedan vacios 
                mainParser.lista[5] = Nodo.Nodo(tokens[lenTokens-1],tokens[lenTokens-1].value,[]) # }
                
                # si no es type o void - token inesperado
                if tokens[3].tipoSimbolo.nommbre != '<type>' and 'void' not in tokens[3].tipoSimbolo.regEx  and lenTokens >= 5 :
                    listaErrores.append("Parse error: Token inesperado! " + tokens[3].value + " linea " + str(tokens[3].id))
                else: # si es type o void
                    countField = 3 # 3 por class program {
                    countIndex = 3
                    # mientras sea == id, ',' , ';' , type 
                    while (tokens[countField].tipoSimbolo.nommbre == '<id>' or ',' == tokens[countField].value or ';' == tokens[countField].value or tokens[countField].tipoSimbolo.nommbre == '<type>') and countField < lenTokens-1:
                        if ';' == tokens[countField].value:
                            countIndex = countField
                        countField += 1
                    
                    fieldList = [] # var declaradas
                    if 3 != countIndex :
                        fieldList = tokens[3:countIndex +1] # despues de { hasta ;

                    listaFieldNodo = []
                    for fToken in fieldList:
                        listaFieldNodo.append(Nodo.Nodo(fToken, fToken.value, []))

                    fieldNodo = Nodo.Nodo("<fieldList>", "fieldList", listaFieldNodo) 
                    # llenamos el lista[3] con las vars declaradas
                    mainParser.lista[3] = fieldNodo
                    
                    #Method todos los mets del codigo
                    if len(listaFieldNodo) == 0 :
                        listaMethod = tokens[countIndex:lenTokens-1]
                    else:
                        listaMethod = tokens[countIndex+1:lenTokens-1] #despues de ; hasta el ult
                    
                    listaMethodNodo = []
                    for token in listaMethod:
                        listaMethodNodo.append(Nodo.Nodo(token, token.value, [])) 

                    methodNodo = Nodo.Nodo("<listaMethod>", "listaMethod", listaMethodNodo)
                    # llenamos el lista[4] con los metodos de la clase
                    mainParser.lista[4] = methodNodo
                    ya = True # la lista de program esta llena
        if ya:
            parseM = ParseMethods.ParseMethods()
            parseM.fieldParse(mainParser, mainParser.lista[3], 'fieldList', debug, listaErrores)
            parseM.metParse(mainParser, mainParser.lista[4], 'listaMethod', debug, listaErrores)
        
        # llenamos el lista[5] con el parse del block
        for bloque in mainParser.obtMethodDeclList(): # for i in bloques
            bloque.lista[5] = parseM.blockParse(mainParser, bloque.lista[5], debug, listaErrores)

        # parseM.accepts(tokens)

        if debug:
            print(listaErrores)
            print("------------------------")

        # print("\nLISTA MAIN")
        # for i in mainParser.lista:
        #     try:
        #         print(i.nodo.prettyPrint())
        #     except:
        #         print("• ",i.nodo)
        #         # for j in i.lista:
        #         #     for nodo in j.lista:
        #         #         for var in nodo.lista:
        #         #             print(var.nodo.prettyPrint())
        # print("")
        
        # # ARBOL
        mainParser.obtNodosAll()
        ast = mainParser.ProgramTree
        for pre, fill, node in RenderTree(ast):
            print("%s%s" % (pre, node.name))

        # siguiente devolver Main
        return mainParser, listaErrores
