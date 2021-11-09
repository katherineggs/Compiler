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

        # print("Field")
        # for i in lista:
        #     print(i.nodo.prettyPrint())

        if tipoDFA == 'fieldList' :
            listaNodos0 = []
            contBsN = 0
            listacontB = []
            
            for i in lista:
                if ';' == i.nodo.value :
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

            # print("Lista Field")            
            # for i in listaField:
            #     print("lista")
            #     print(i)
            #     for lis in i:
            #         print(lis.nodo.prettyPrint())
            
            for varDecl in listaField: #nodos
                if len(varDecl) < 3 : # minio deben haber 3 -- type id ;
                    listaErrores.append("Parse error: No hay suficientes tokens en la declaracion! linea - " + str(varDecl[0].nodo.id))
                
                if len(varDecl) == 3 :
                    if varDecl[0].nodo.tipoSimbolo.nommbre != '<type>' :
                        listaErrores.append("Parse error: Token inesperado " + varDecl[0].nodo.tipoSimbolo.nommbre + " linea - " + str(varDecl[0].nodo.id))
                    if varDecl[1].nodo.tipoSimbolo.nommbre != '<id>' :
                        listaErrores.append("Parse error: Token inesperado " + varDecl[1].nodo.tipoSimbolo.nommbre + " linea - " + str(varDecl[1].nodo.id))
                    if ';' != varDecl[2].nodo.value :
                        listaErrores.append("Parse error: Token inesperado " + varDecl[2].nodo.value + " linea - " + str(varDecl[2].nodo.id))
                    if varDecl[0].nodo.tipoSimbolo.nommbre == '<type>' and varDecl[1].nodo.tipoSimbolo.nommbre == '<id>' and ';' == varDecl[2].nodo.value :
                        objField = field.FieldDecl()
                        listaNodos0.append(nodoA.Nodo(objField, "varDecl", [varDecl[0], varDecl[1], varDecl[2]]))
                
                if len(varDecl) > 3 :
                    idField = []
                    idSeguir = True
                    if varDecl[0].nodo.tipoSimbolo.nommbre != '<type>' :
                        listaErrores.append("Parse error: Token inesperado " + varDecl[0].nodo.tipoSimbolo.nommbre + " linea - " + str(varDecl[0].nodo.id))
                        idSeguir = False
                    
                    for i in range(1, len(varDecl)-1):  #quitamos type y ;
                        if i % 2 != 0: # no es par VER SI TIENE ID
                            if varDecl[i].nodo.tipoSimbolo.nommbre != '<id>' :
                                listaErrores.append("Parse error: Token inesperado " + varDecl[i].nodo.tipoSimbolo.nommbre + " linea - " + str(varDecl[i].nodo.id))
                                idSeguir = False
                            else:
                                idField.append(varDecl[i])
                        else:
                            if ',' != varDecl[i].nodo.value :
                                if varDecl[i].nodo.tipoSimbolo.nommbre == "<type>":
                                    listaErrores.append("Parse error: Token inesperado falta " + ";" + " linea - " + str(varDecl[i].nodo.id-1))
                                
                                else:
                                    listaErrores.append("Parse error: Token inesperado falta " + "," + " linea - " + str(varDecl[i].nodo.id))
                                idSeguir = False

                    if idSeguir :
                        for i in idField:
                            objField = field.FieldDecl()
                            listaNodos0.append(nodoA.Nodo(objField, "varDecl", [varDecl[0], i, varDecl[len(varDecl)-1]]))

            nodoPrinc.lista = listaNodos0
            Program.lista[3] = nodoPrinc

        if debug :
            print("Lista Errores", listaErrores)
    # las funcs o todo lo demas 
    def metParse(self, Program, nodoPrinc, tipoDFA, debug, listaErrores):
        listaMethod = []
        lista = nodoPrinc.lista

        # print("Method")
        # for i in lista[:-3]:
        #     print(i.nodo.prettyPrint())

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
                # print(indexsN)
                if indexsN < (len(lista) - 3) : # los ult 2 no
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
                                # print(lista[countM+1].nodo.prettyPrint())
                                # print(lista[countM+2].nodo.prettyPrint())
                                # print("s")
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

    def blockParse(self, Program, nodoPrinc, debug, listaErrores):
        nodoPrincipal = nodoA.Nodo("$", "$", [])
        # states = [0]
        stackNodos = [nodoPrincipal.nodo]

        revisarLista = nodoPrinc.lista

        # print("LISTA")
        # for i in revisarLista:
        #     # for j in i:
        #     print(i.nodo.prettyPrint())
                
        tamanoRev = len(revisarLista)
        contB = 0

        while contB < tamanoRev :
            nodoActual = revisarLista[contB]

            param = nodoActual.nodo.tipoSimbolo.nommbre
            param = param.replace("<","")
            param = param.replace(">","")
            
            # SHIFT
            if param != "signos" :
                if param == "reservedW":
                    stackNodos.append(nodoActual.nodo.value)
                else:
                    stackNodos.append(param)
            else:
                stackNodos.append(nodoActual.nodo.value)
            
            contB += 1

            tamanoStack = len(stackNodos)
            for item in gramm.DFAs.gramatica:
                stack2 = stackNodos.copy() 
                for k,v in item.items():

                    contValue = 0
                    while contValue <= tamanoStack:
                        if v == stack2:
                            #REDUCE
                            stackNodos = stackNodos[:-len(v)] 
                            stackNodos.append(k)
                            
                            # print("M",stackNodos)
                            
                            newT = len(stackNodos)
                            for it in gramm.DFAs.gramatica:
                                stack3 = stackNodos.copy()
                                for a,b in it.items():
                                    miniCont = 0
                                    while miniCont <= newT:
                                        if b == stack3:
                                            #REDUCE
                                            stackNodos = stackNodos[:-len(b)] 
                                            stackNodos.append(a)
                                            break
                                        else:
                                            if len(stack3) > 0:
                                                # print("else")
                                                stack3.pop(0)
                                            else:
                                                break
                                        miniCont += 1
                            
                            # print("F",stackNodos)
                            # print("BUENAaaaas----------------------------\n")
                            break
                        else:
                            if len(stack2) > 0:
                                # print("else")
                                stack2.pop(0)
                            else:
                                break
                        contValue += 1
                        # print(contValue)
        
        print(stackNodos)
        # print(stackNodos[2:])
        # result = all(element == stackNodos[2] for element in stackNodos[2:])
        # print(result)
            

        # print("\nSTACK")
        # for i in stackNodos:
        #     print(i)

        if debug :
            print(listaErrores)

        if len(listaErrores) == 0 :
            return stackNodos[-1]
        else:
            return nodoA.Nodo("block", "block", [])

def recMethod(stackNodos):
    tamanoStack = len(stackNodos)
    for item in gramm.DFAs.gramatica:
        stack2 = stackNodos.copy() 
        for k,v in item.items():
            contValue = 0
            while contValue <= tamanoStack:
                if v == stack2:
                    #REDUCE
                    stackNodos = stackNodos[:-len(v)] 
                    stackNodos.append(k)
                    recMethod(stackNodos)
                    print("F",stackNodos)
                    break
                else:
                    if len(stack2) > 0:
                        # print("else")
                        stack2.pop(0)
                    else:
                        break
                contValue += 1
    return stackNodos

