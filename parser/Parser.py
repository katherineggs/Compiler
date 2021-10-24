import abstracts.Symbols as Symbol
import abstracts.Tokens as Token
import abstracts.Node as Nodo
import abstracts.Program as Program
import DFAs as DFAs
import re

class Parser:
    def parser(self, tokens, debug):
        mainParser = Program.Program(['', '', '', '', '', ''])
        listaErrores = []
        lenTokens = len(tokens)
        ya = False 

        if lenTokens < 4 :
            print("No hay suficientes tokens")
        else:
            if tokens[0].tipoSimbolo.nommbre != 'class' :
                listaErrores.append("Parse error, Falta - class token")
            
            if tokens[1].tipoSimbolo.nommbre != 'Program' :
                listaErrores.append("Parse error, Falta - nommbre of class token")

            if tokens[2].tipoSimbolo.nommbre != '{' :
                listaErrores.append("Parse error, Falta - first { token")

            if tokens[lenTokens-1].tipoSimbolo.nommbre != '}' :
                listaErrores.append("Parse error, Falta - last closing } token")

            if tokens[0].tipoSimbolo.nommbre == 'class' and tokens[1].tipoSimbolo.nommbre == 'Program' and tokens[2].tipoSimbolo.nommbre == '{' and tokens[lenTokens-1].tipoSimbolo.nommbre == '}' :
                mainParser.lista[0] = Nodo.Nodo(tokens[0], tokens[0].tipoSimbolo.nommbre, [])
                mainParser.lista[1] = Nodo.Nodo(tokens[1],tokens[1].tipoSimbolo.nommbre,[])
                mainParser.lista[2] = Nodo.Nodo(tokens[2],tokens[2].tipoSimbolo.nommbre,[])
                mainParser.lista[5] = Nodo.Nodo(tokens[lenTokens-1],tokens[lenTokens-1].tipoSimbolo.nommbre,[])

                if tokens[3].tipoSimbolo.nommbre != 'type' and tokens[3].tipoSimbolo.nommbre != 'void' and lenTokens>=5 :
                    listaErrores.append("Parse error: Unexpected token " + tokens[3].tipoSimbolo.nommbre + " at line " + str(tokens[3].line))
                else:
                    countField = 3
                    countIndex = 3
                    while (tokens[countField].tipoSimbolo.nommbre == 'id' or tokens[countField].tipoSimbolo.nommbre == ',' or tokens[countField].tipoSimbolo.nommbre == ';' or tokens[countField].tipoSimbolo.nommbre == 'type') and countField<lenTokens-1:
                        if tokens[countField].tipoSimbolo.nommbre == ';':
                            countIndex = countField
                        countField += 1
                    fieldList = []
                    if 3 != countIndex :
                        fieldList = tokens[3:countIndex +1]

                    listaFieldNodo = []
                    for token in fieldList:
                        listaFieldNodo.append(Nodo.Nodo(token, token.tipoSimbolo.nommbre, []))

                    fieldNodo = Nodo.Nodo("<fieldList>", "fieldList", listaFieldNodo)
                    mainParser.lista[3] = fieldNodo
                    
                    if len(listaFieldNodo) == 0 :
                        listaMethod = tokens[countIndex:lenTokens-1]
                    else:
                        listaMethod = tokens[countIndex+1:lenTokens-1]
                    listaMethodNodo = []
                    
                    for token in listaMethod:
                        listaMethodNodo.append(Nodo.Nodo(token, token.tipoSimbolo.nommbre, []))              

                    methodNodo = Nodo.Nodo("<listaMethod>", "listaMethod", listaMethodNodo)
                    mainParser.lista[4] = methodNodo
                    ya = True

        if ya:
            dfa = DFAs.DFAs()
            dfa.fieldParse(mainParser, mainParser.lista[3], 'fieldList', debug, listaErrores)
            dfa.metParse(mainParser, mainParser.lista[4], 'listaMethod', debug, listaErrores)

            for method in mainParser.obtMethodDeclList():
                method.lista[5] = dfa.blockParse(mainParser, method.lista[5], debug, listaErrores)

        if debug:
            print(listaErrores)

        # siguiente devolver Main
        return listaErrores