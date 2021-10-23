from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter
import objects.IrtNode as IrtNode

class Program:

    def __init__(self, lista):
        self.lista = lista
        self.type = "Program"
        self.symbolTabla = []
        self.nodosCompletos = []
        self.ProgramTree = ''
        self.irtLista = []
        self.puntero = 0

    def obtNodosAll(self):
        ProgramUI = Node_any("Program")
        self.ProgramTree = ProgramUI
        cont=0
        for nodoL in self.lista:
            nodoAny = Node_any(nodoL.tipo + ' ' + str(cont), parent = ProgramUI)
            self.nodosCompletos.append(nodoL.tipo + ' ' +str(cont))
            cont+=1
            if (len(nodoL.lista)!=0):
                cont = nodoL.getNodes(self.nodosCompletos, cont, nodoAny)
   
    def obtNodosAllIrt(self):
        self.irtLista.append(IrtNode.IrtNode("Program", ["StartProgram"]))

        cont=0
        for nodoL in self.lista:
            nodoL.getIrtInstructions(self.irtLista, self.symbolTabla, cont)
            cont+=1

        self.irtLista.append(IrtNode.IrtNode("Program", ["EndProgram"]))


    def obtFieldDeclList(self):
        return self.lista[3].lista

    def obtMethodDeclList(self):
        return self.lista[4].lista 