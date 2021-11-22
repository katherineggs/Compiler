import re
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

import abstracts.Symbols as Symbols
import abstracts.Tokens as Tokens
import abstracts.Node as Node
import abstracts.Program as Program
import parser1.DFAs as DFAs


class Irt:
    def irt(self, mainProgram, debug):
        # print(mainProgram, debug, mainProgram.simbs)
        mainProgram.obtNodosAll()

        mainProgram.obtNodosAllIrt()
        # print(mainProgram.listaIrt)
        if(debug):
            for nodoIrt in mainProgram.listaIrt:
                try:
                    # print(nodoIrt.type_irt)
                    print(nodoIrt.instruccion)
                except:
                    print("no hay un nodo irt")
        
        return mainProgram.listaIrt