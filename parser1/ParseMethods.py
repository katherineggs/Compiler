import abstracts.Node as nodoA
import abstracts.FieldDecl as field
import abstracts.MethodDecl as metodo
import abstracts.VarDeclList as listaVariables
import abstracts.Block as block
import parser1.DFAs as gramm

class ParseMethods:
    # Variables de la clase
    def fieldParse(self, Program, nodoPrinc, tipoDFA, debug, listaErrores):
        lista = nodoPrinc.lista

        if tipoDFA == 'fieldList' :
            listaNodos0 = []
            contBsN = 0
            listacontB = []
            
            for i in lista:
                if ';' in i.nodo.tipoSimbolo.regEx :
                    listacontB.append(contBsN) # append del index que tenga ;
                contBsN += 1          

            listaField = [] # lista de listas con vars desde id hasta ;
            for split in range(len(listacontB)) :
                if split == 0 :
                    # variable 1 desde id hasta ;
                    listaField.append(lista[0:listacontB[split] + 1]) 
                else:
                    # demas vars desde id hasta ;
                    listaField.append(lista[listacontB[split - 1] + 1:listacontB[split] + 1])
                    
            for fieldDecl in listaField: #nodos
                if len(fieldDecl) < 3 : # minio deben haber 3 -- type id ;
                    listaErrores.append("Parse error: No hay suficientes tokens en la declaracion! linea - " + str(fieldDecl[0].nodo.id))
                
                if len(fieldDecl) == 3 :
                    if fieldDecl[0].nodo.tipoSimbolo.nommbre != '<type>' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[0].nodo.tipoSimbolo.nommbre + " linea - " + str(fieldDecl[0].nodo.id))
                    if fieldDecl[1].nodo.tipoSimbolo.nommbre != '<id>' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[1].nodo.tipoSimbolo.nommbre + " linea - " + str(fieldDecl[1].nodo.id))
                    if ';' != fieldDecl[2].nodo.value :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[2].nodo.value + " linea - " + str(fieldDecl[2].nodo.id))
                    if fieldDecl[0].nodo.tipoSimbolo.nommbre == '<type>' and fieldDecl[1].nodo.tipoSimbolo.nommbre == '<id>' and ';' == fieldDecl[2].nodo.value :
                        objField = field.FieldDecl()
                        listaNodos0.append(nodoA.Nodo(objField, "fieldDecl", [fieldDecl[0], fieldDecl[1], fieldDecl[2]]))
                
                if len(fieldDecl) > 3 :
                    idField = []
                    idSeguir = True
                    if fieldDecl[0].nodo.tipoSimbolo.nommbre != '<type>' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[0].nodo.tipoSimbolo.nommbre + " linea - " + str(fieldDecl[0].nodo.id))
                        idSeguir = False
                    for i in range(1, len(fieldDecl)-1): #quitamos type y ;
                        if i % 2 != 0: # si es par
                            if fieldDecl[i].nodo.tipoSimbolo.nommbre != '<id>' :
                                listaErrores.append("Parse error: Token inesperado " + fieldDecl[i].nodo.tipoSimbolo.nommbre + " linea - " + str(fieldDecl[i].nodo.id))
                                idSeguir = False
                            else:
                                idField.append(fieldDecl[i])
                        else:
                            if ',' != fieldDecl[i].nodo.value :
                                listaErrores.append("Parse error: Token inesperado " + "," + " linea - " + str(fieldDecl[i].nodo.id))
                                idSeguir = False
                    if idSeguir :
                        for i in idField:
                            objField = field.FieldDecl()
                            listaNodos0.append(nodoA.Nodo(objField, "fieldDecl", [fieldDecl[0], i, fieldDecl[len(fieldDecl)-1]]))

            nodoPrinc.lista = listaNodos0
            Program.lista[3] = nodoPrinc

        if debug :
            print("Lista Errores", listaErrores)
    # todo lo demas
    def metParse(self, Program, nodoPrinc, tipoDFA, debug, listaErrores):
        listaMethod = []
        lista = nodoPrinc.lista

        if len(lista) < 6 : #type, id,(, ), {, }
            listaErrores.append("Parse error: su method no tiene suficientes tokens!")
        else:
            if lista[0].nodo.tipoSimbolo.nommbre != "<type>" and "void" != lista[0].nodo.value :
                listaErrores.append("Parse error: Token inesperado " + lista[0].nodo.tipoSimbolo.nommbre + " linea - " + str(lista[0].nodo.id))
            if lista[1].nodo.tipoSimbolo.nommbre != "<id>" :
                listaErrores.append("Parse error: Token inesperado " + lista[1].nodo.tipoSimbolo.nommbre + " linea - " + str(lista[1].nodo.id))
            if "(" != lista[2].nodo.value :
                listaErrores.append("Parse error: Token inesperado " + lista[2].nodo.value + " linea - " + str(lista[2].nodo.id))
            
            for indexsN in range(len(lista)) :
                if indexsN < (len(lista) - 3) : # los ult 3 no
                    # if - type id (
                    if (lista[indexsN].nodo.tipoSimbolo.nommbre == "<type>" or "void" == lista[indexsN].nodo.value) and lista[indexsN+1].nodo.tipoSimbolo.nommbre == "<id>" and "(" == lista[indexsN+2].nodo.value:
                        # Nodo method 
                        metodoObj = metodo.MethodDecl()
                        metodoNodo = nodoA.Nodo(metodoObj, "methodDecl", [lista[indexsN], lista[indexsN + 1], lista[indexsN + 2]])
                        listaMethod.append(metodoNodo)

                        countM = indexsN + 3 # ya tenemos los p3
                        varHijo = []
                        seguir = True

                        # hasta encontrar )
                        while ")" != lista[countM].nodo.value and countM < (len(lista) - 3):
                            seguir = True
                            # si tenemos ( type
                            if lista[countM].nodo.tipoSimbolo.nommbre == "<type>" :
                                if lista[countM+1].nodo.tipoSimbolo.nommbre != "<id>" or ("," != lista[countM+2].nodo.value and ")" != lista[countM+2].nodo.value) :
                                    listaErrores.append("Parse error: Token inesperado " + lista[countM].nodo.tipoSimbolo.nommbre + " linea - " + str(lista[countM].nodo.id))
                                    seguir = False
                                else: # (type id  / (type algo , y )
                                    varHijo.append(lista[countM])

                            # si tenemos ( id
                            elif lista[countM].nodo.tipoSimbolo.nommbre == "<id>" :
                                if (","  != lista[countM+1].nodo.value and ")" != lista[countM+1].nodo.value) or lista[countM-1].nodo.tipoSimbolo.nommbre != "<type>" :
                                    listaErrores.append("Parse error: Token inesperado " + lista[countM].nodo.tipoSimbolo.nommbre + " linea - " + str(lista[countM].nodo.id))
                                    seguir = False
                                else:
                                    varHijo.append(lista[countM])
                            # si tenemos ( ,
                            elif "," == lista[countM].nodo.value :
                                if lista[countM+1].nodo.tipoSimbolo.nommbre != "<type>" or lista[countM-1].nodo.tipoSimbolo.nommbre != "<id>" :
                                    listaErrores.append("Parse error: Token inesperado "+ lista[countM].nodo.tipoSimbolo.nommbre + " linea - " + str(lista[countM].nodo.id))
                                    seguir = False
                                else:
                                    varHijo.append(lista[countM])
                            else:
                                listaErrores.append("Parse error: Token inesperado "+ lista[countM].nodo.value + " linea - " + str(lista[countM].nodo.id))
                                seguir = False
                            countM += 1

                        if ")" != lista[countM].nodo.value :
                            listaErrores.append("Parse error: Falta ')' en la declaracion del metodo")

                        varObj = listaVariables.VarDeclList()
                        varNodo = nodoA.Nodo(varObj, "listaVarDecl", [])

                        if seguir :
                            varNodo.lista = varHijo
                        metodoNodo.lista.append(varNodo)
                        metodoNodo.lista.append(lista[countM])
                        countM += 1

                        # tenemos ya type id ()
                        blockHijos = []
                        if "{" == lista[countM].nodo.value  :
                            # despues de { que no sea id & (
                            while not(lista[countM+1].nodo.tipoSimbolo.nommbre == "<id>" and "(" == lista[countM+2].nodo.value) and countM<len(lista)-2:
                                blockHijos.append(lista[countM])
                                countM += 1
                            if countM == len(lista) -2 :
                                blockHijos.append(lista[countM])
                                blockHijos.append(lista[countM+1])                              
                        # print("BLOCK")
                        # for i in blockHijos:
                        #     print(i.nodo.prettyPrint())
                        
                        # Nodo block
                        blockObj = block.Block()
                        blockNodo = nodoA.Nodo(blockObj, "block", blockHijos)
                        metodoNodo.lista.append(blockNodo)

            nodoPrinc.lista = listaMethod
            Program.lista[4] = nodoPrinc
        if debug:
            print(listaErrores)
