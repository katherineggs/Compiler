from anytree import Node as Node_any

import abstracts.IrtNode as IrtNode

class Program:

    def __init__(self, lista):
        self.lista = lista
        self.type = "Program"
        self.simbs = []
        self.puntero = 0
        self.nodosCompletos = []
        self.ProgramTree = ''
        self.listaIrt = []

    def obtNodosAll(self):
        ProgramUI = Node_any("Program")
        self.ProgramTree = ProgramUI
        cont=0
        for nodoL in self.lista:
            nodoAny = Node_any(nodoL.tipo + ' ' + str(cont), parent = ProgramUI)
            self.nodosCompletos.append(nodoL.tipo + ' ' +str(cont))
            cont+=1
            if (len(nodoL.lista)!=0):
                cont = nodoL.obtNodos(self.nodosCompletos, cont, nodoAny)
   
    def obtFieldDeclList(self):
        return self.lista[3].lista

    def obtMethodDeclList(self):
        return self.lista[4].lista 

    def obtNodosAllIrt(self):
        self.listaIrt.append(IrtNode.IrtNode("Program", ["StartProgram"]))

        cont = 0
        for node in self.lista:
            node.obtIrtInstructions(self.listaIrt, self.simbs, cont)
            cont += 1
            # if (len(node.lista)!=0):
            #     cont = node.getNodesIrt(self.listaIrt, self.simbs, cont)

        self.listaIrt.append(IrtNode.IrtNode("Program", ["EndProgram"]))