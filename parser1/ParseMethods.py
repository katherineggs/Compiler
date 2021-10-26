import abstracts.Node as nodoA
import abstracts.FieldDecl as field
import abstracts.MethodDecl as metodo
import abstracts.VarDeclList as listaVariables
import abstracts.Block as block
import parser1.DFAs as gramm

class ParseMethods:

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
                        
                        # Nodo block
                        blockObj = block.Block()
                        blockNodo = nodoA.Nodo(blockObj, "block", blockHijos)
                        metodoNodo.lista.append(blockNodo)

            nodoPrinc.lista = listaMethod
            Program.lista[4] = nodoPrinc
        if debug:
            print(listaErrores)

    def blockParse(self, Program, nodoPrinc, debug, listaErrores):
        nodoPrincipal = nodoA.Nodo("$", "$", [])
        states = [0]
        stackNodos = [nodoPrincipal]

        revisarLista = nodoPrinc.lista

        # for i in revisarLista:
        #     print(i.nodo.prettyPrint())
        
        tamanoRev = len(revisarLista)
        contB = 0
        ultEstado = states[-1]
        parametros = []
        nodoActual = revisarLista[ultEstado]
        parametros = gramm.DFAs.dfa.get(ultEstado).get(nodoActual.tipo)
        print("TIPO")
        print(nodoActual.tipo)
        print(gramm.DFAs.dfa.get(ultEstado))
        print("PARAMETROS")
        print(parametros)

        if parametros == None :
            listaErrores.append("Parse error: FALTA { linea - " + str(nodoActual.nodo.id))

        contWhile = 0
        while contB < tamanoRev and contWhile < 15 :
            if parametros != None :
                if parametros[0] == 'shift' :
                    stackNodos.append(nodoActual)
                    states.append(parametros[1])
                    contB += 1
                    nodoActual = revisarLista[contB]
                    parametros = gramm.DFAs.dfa.get(states[-1]).get(nodoActual.tipo)

                elif parametros[0] == 'goTo' :
                    # no al stack
                    states.append(parametros[1])
                    # se mantiene el nodo y los param
                    nodoActual = revisarLista[contB]
                    parametros = gramm.DFAs.dfa.get(states[-1]).get(nodoActual.tipo)

                elif parametros[0] == 'reduce' :
                    if parametros[1] == 2 :  
                        temp = []
                        abrir = ""
                        for nod in stackNodos[::-1]:
                            print("NOD.TIPO")
                            print(nod.tipo)
                            if nod.tipo == "statement" :
                                temp.append(nod)
                            elif nod.tipo == "{" :
                                abrir = nod
                                break
                            else:
                                listaErrores.append("Parsing error, Elemento inesperado " + nod.tipo)
                                break

                        statementNodos = nodoA.Nodo("statementList", "statementList", temp[::-1])
                        blockNodo = nodoA.Nodo("block", "block", [abrir, statementNodos, revisarLista[contB]])
                        count = len(temp) + 1
                        stackNodos = stackNodos[:-count]
                        states = states[:-(count)]
                        stackNodos.append(blockNodo)
                        contB += 1

                        parametros = gramm.DFAs.dfa.get(states[-1]).get(blockNodo.tipo)

                    else:
                        nodo = list(gramm.DFAs.gramatica[parametros[1]-1].keys())[0]
                        tipo = list(gramm.DFAs.gramatica[parametros[1]-1].keys())[0]
                        count = len(list(gramm.DFAs.gramatica[parametros[1]-1].values())[0])

                        listaHijos = stackNodos[-count:]

                        stackNodos = stackNodos[:-count]

                        states = states[:-(count)]
                        nuevoN = nodoA.Nodo(nodo, tipo, listaHijos)

                        stackNodos.append(nuevoN)
                        parametros = gramm.DFAs.dfa.get(states[-1]).get(nuevoN.tipo)

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "!" :
                                parametros = ['goTo', 58]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "menos" and stackNodos[-3].tipo != "expr" :
                                parametros = ['goTo', 58]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if revisarLista[contB].tipo == "{" and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "," and stackNodos[-3].tipo == "expr" :
                                parametros = ['goTo', 81]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if revisarLista[contB].tipo == ")" and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "(" and stackNodos[-3].tipo != "if" :
                                parametros = ['goTo', 59]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "menos" and stackNodos[-3].tipo == "expr" :
                                parametros = ['goTo', 69]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "binOp" and stackNodos[-3].tipo == "expr" :
                                parametros = ['goTo', 69]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if revisarLista[contB].tipo == ")" and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "(" and stackNodos[-3].tipo == "if" :
                                parametros = ['goTo', 44]

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if revisarLista[contB].tipo == "," and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "assignOperators" :
                                parametros = ['goTo', 65]

                elif parametros[0] == 'accept' :
                    print("Aceptado!")
            else:
                # Estado no definido
                if contB < len(revisarLista):
                    listaErrores.append("Parse error: Token inesperado " + revisarLista[contB].tipo + " linea - " + str(revisarLista[contB].nodo.id))
                else:
                    listaErrores.append("Parse error: Token inesperado " + revisarLista[contB-1].tipo + " linea - " + str(revisarLista[contB-1].nodo.id))
                break

        if debug :
            print(listaErrores)

        if len(listaErrores) == 0 :
            return stackNodos[-1]
        else:
            return nodoA.Nodo("block", "block", [])
    
    def accepts(self, listaTokens):
        state = 0
        contAccepts = 0
        parametros=[]

        print(len(listaTokens))

        tokenActual = listaTokens[contAccepts].tipoSimbolo.nommbre
        parametros = gramm.DFAs.dfa.get(state).get(tokenActual)

        print(parametros)

        while contAccepts <= len(listaTokens) :
            #print(listaTokens[contAccepts].tipoSimbolo.nommbre)
            print(state)
            if parametros != None :
                if parametros[0] == 'shift' :
                    tokenActual = listaTokens[contAccepts].tipoSimbolo.nommbre
                    gramm.DFAs.tokens.append(tokenActual)
                    parametros = gramm.DFAs.dfa.get(gramm.DFAs.states[-1]).get(tokenActual)
                    gramm.DFAs.states.append(parametros[1])
                    contAccepts += 1

                    if contAccepts < len(listaTokens) :
                        tokenActual = listaTokens[contAccepts].tipoSimbolo.nommbre
                    parametros = gramm.DFAs.dfa.get(gramm.DFAs.states[-1]).get(tokenActual)
                    print("shift")

                elif parametros[0] == 'goTo' :
                    print(tokenActual)
                    print(parametros[1])
                    gramm.DFAs.states.append(parametros[1])
                    
                    if contAccepts < len(listaTokens) :
                        tokenActual = listaTokens[contAccepts].tipoSimbolo.nommbre
                        parametros = gramm.DFAs.dfa.get(gramm.DFAs.states[-1]).get(tokenActual)
                    else:
                        print(parametros)
                        gramm.DFAs.tokens.pop(-1)
                        gramm.DFAs.states.pop(-1)
                        break
                    print('goTo')
                
                elif parametros[0] == 'reduce' :
                    print(parametros[1])
                    node = nodoA.Nodo(list(gramm.DFAs.gramaticaProgram[parametros[1]-1].keys())[0], list(gramm.DFAs.gramaticaProgram[parametros[1]-1].values())[0])
                    count = len(list(gramm.DFAs.gramaticaProgram[parametros[1]-1].values())[0])
                    gramm.DFAs.tokens = gramm.DFAs.tokens[:-count]
                    gramm.DFAs.states = gramm.DFAs.states[:-(count)]
                    gramm.DFAs.tokens.append(list(gramm.DFAs.gramaticaProgram[parametros[1]-1].keys())[0])
                    tokenActual = gramm.DFAs.tokens[-1]
                    print(gramm.DFAs.states)
                    parametros = gramm.DFAs.dfa.get(gramm.DFAs.states[-1]).get(tokenActual)

                    print("Lista nodos", node.listaTokens)
                    print("Nodo - ", node)
                    print("reduce")

                elif parametros[0] == 'accept' :
                    print("Acepatdo!")
            else:
                print("Estado no definido")
                if contAccepts < len(listaTokens) :
                    print("Token inesperado",listaTokens[contAccepts].tipoSimbolo.nommbre," linea - ",listaTokens[contAccepts].id)
                else:
                    print("Token inesperado",listaTokens[contAccepts-1].tipoSimbolo.nommbre," linea - ",listaTokens[contAccepts-1].id)
                break
            print(gramm.DFAs.tokens)
            print(gramm.DFAs.states)
            print("------")

        print(gramm.DFAs.states)
        print(gramm.DFAs.tokens)
        if(len(gramm.DFAs.tokens)==1 and len(gramm.DFAs.states)==1):
            print("Parseo Completo")
        else:
            print("Parseo Invalido")
        return True