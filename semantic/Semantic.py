class Semantic:
    def semantic(self, mainProgram, debug):
        listaErrores = []
        #scope y declaración de variables

        # symbol table
        cont = 0
        
        for nodoL in mainProgram.lista:
            print("")
            if(len(nodoL.lista) == 0 and str(type(nodoL.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and nodoL.nodo.value == "{"):
                mainProgram.simbs.append([])

            if(len(nodoL.lista) == 0 and str(type(nodoL.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and nodoL.nodo.value == "}"):
                pass
            cont += 1

            if (len(nodoL.lista) != 0):
                #print(mainProgram.simbs)
                cont = nodoL.analisisSemantico(mainProgram.simbs, cont, listaErrores, mainProgram.puntero)
               # print(cont)
                #print(mainProgram.simbs)

        fp = 4
        for symbol in mainProgram.simbs:
            for sym in symbol:
                sym[3] = "$fp-" + str(fp)
                fp += 4

        if(debug):
            for symbol in mainProgram.simbs:
                print(symbol)
            print("listaErrores", listaErrores)
        return listaErrores
