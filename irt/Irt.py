class Irt:
    def irt(self, mainProgram, debug):
        # print(mainProgram, debug, mainProgram.simbs)
        mainProgram.obtNodosAll()
        # print("CLASS")
        # print(mainProgram.obtNodosAll())
        # print(mainProgram.obtNodosAllIrt())

        mainProgram.obtNodosAllIrt()

        # print(mainProgram.listaIrt)
        
        if debug:
            for nodoIrt in mainProgram.listaIrt:
                try:
                    # print(nodoIrt.type_irt)
                    print(nodoIrt.instruccion)
                except:
                    print("no hay un nodo irt")
        
        return mainProgram.listaIrt