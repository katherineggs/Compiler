from anytree import Node as Node_any

class MethodDecl:
    def __init__(self, nodo = "", tipo = "methodDecl", lista = ""):
        self.nodo = nodo
        self.tipo = tipo
        self.lista = lista

    def obtNodos(self, Program, cont, nodoPrinc):
        if(len(self.lista)!=0 and self.nodo!='methodDeclList'):
            for nodoL in self.lista:
                nodoAny = Node_any(nodoL.nodo + str(cont), parent = nodoPrinc)
                Program.append(nodoL.nodo + str(cont))
                cont+=1
                if(len(nodoL.lista)!=0):
                    cont = nodoL.obtNodos(Program, cont, nodoAny)
        return cont