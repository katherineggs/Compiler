from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter


class Nodo:
    def __init__(self, nodo, tipo, lista):
        self.nodo = nodo
        self.tipo = tipo
        self.lista = lista
    
    def valorMin(self, simbs, cont):
        if self.tipo == "expr":
            if self.lista[0].tipo == "location" :
                for i in simbs[::-1]:
                    for j in i:
                        if self.lista[0].lista[0].nodo.value == j[1]:
                            tipoFinal = j[3]
                            return str(tipoFinal)

            elif self.lista[0].tipo == "literal" :
                if self.lista[0].lista[0].tipo == "intLiteral" :
                    return str(self.lista[0].lista[0].nodo.value)

                if self.lista[0].lista[0].tipo == "stringLiteral" :
                    return str(self.lista[0].lista[0].nodo.value)

                if self.lista[0].lista[0].tipo == "charLiteral" :
                    return str(self.lista[0].lista[0].nodo.value) 

                if self.lista[0].lista[0].tipo == "boolLiteral" :
                    return str(self.lista[0].lista[0].nodo.value) 

            # Rec
            elif self.lista[0].tipo == "(" :
                return self.lista[1].valorMin(simbs, cont)
            
            # binOp = ⟨arith op⟩ | ⟨rel op⟩ | ⟨eq op⟩ | ⟨cond op⟩
            elif len(self.lista) == 3 and self.lista[0].tipo == "expr" and self.lista[1].tipo == "binOp" and self.lista[2].tipo == "expr" :      
                return [self.lista[0].valorMin(simbs, cont), self.lista[1].valorMin(simbs, cont), self.lista[2].valorMin(simbs, cont)]
            
            elif len(self.lista) == 1 and self.lista[0].tipo == "expr" :
                return self.lista[0].valorMin(simbs, cont)
            
            else:
                return "minValue"
        
        elif self.tipo == "binOp" :
            if self.lista[0].tipo == "equalityOperatos" :
                return self.lista[0].nodo.value
            
            elif self.lista[0].tipo == "operadores" :
                return self.lista[0].nodo.value
            
            elif self.lista[0].tipo == "conditionOperators" :
                return self.lista[0].nodo.value
            
            else:
                return "minValue"
        
        elif self.tipo == "assignOperators" :
            return self.nodo.value

        elif self.tipo == "location" :
            for i in simbs[::-1]:
                for j in i:
                    if self.lista[0].nodo.value == j[1]:
                        tipoFinal = j[3]
                        return str(tipoFinal)
                        
        elif(self.tipo == "id"):
            for i in simbs[::-1]:
                for j in i:
                    if self.nodo.value == j[1]:
                        tipoFinal = j[3]
                        return str(tipoFinal)
        else:
            return "valorMinimo"

    def obtNodos(self, Program, cont, nodoPrinc):
        if len(self.lista) != 0 and self.tipo != '' :
            for nodoL in self.lista: # nodo de lista
                nodoAny = Node_any(nodoL.tipo + ' ' + str(cont), parent = nodoPrinc)
                Program.append(nodoL.tipo + ' ' + str(cont))
                cont += 1
                if len(nodoL.lista) != 0 :
                    cont = nodoL.obtNodos(Program, cont, nodoAny)
        return cont
    
    def checkTipo(self, simbs, cont, listaErrores):
        print(simbs, cont, listaErrores)

    def obtTipo(self, simbs, listaErrores):
        if self.tipo == 'expr' :
            if self.lista[0].tipo == 'location' :
                tipoFinal = ""
                for i in simbs[::-1]:
                    for j in i:
                        if self.lista[0].lista[0].nodo.value == j[1]:
                            tipoFinal = j[0]
                            break
                return tipoFinal

            if self.lista[0].tipo == 'method_call' :
                tipoFinal = ""
                for i in simbs[::-1]:
                    for j in i:
                        if nodoL.lista[0].lista[0].nodo.value == j[1]:
                            tipoFinal = j[0]
                            break
                return tipoFinal

            if self.lista[0].tipo == 'literal' :
                if self.lista[0].lista[0].tipo == "intLiteral" :
                    return "int"
                if self.lista[0].lista[0].tipo == "charLiteral" :
                    return "char"
                if self.lista[0].lista[0].tipo == "stringLiteral" :
                    return "string"
                if self.lista[0].lista[0].tipo == "boolLiteral" :
                    return "boolean"

            if self.lista[0].tipo == 'expr' :
                if self.lista[1].tipo == 'binOp' :
                    if self.lista[1].lista[0].tipo == 'operadores' :
                        if self.lista[0].obtTipo(simbs, listaErrores) == "int" and self.lista[2].obtTipo(simbs, listaErrores) == "int" :
                            return "int"
                        else:
                            listaErrores.append("Type error: cannot arit_op two things !int")
                            return "typeError"

                    if self.lista[1].lista[0].tipo == 'equalityOperatos' :
                        if self.lista[0].obtTipo(simbs, listaErrores) == self.lista[2].obtTipo(simbs, listaErrores) :
                            return "boolean"
                        else:
                            listaErrores.append("Type error: cannot eq_op two things with diff type")
                            return "typeError"

                    if self.lista[1].lista[0].tipo == 'conditionOperators' :
                        if self.lista[0].obtTipo(simbs, listaErrores) == "boolean" and self.lista[2].obtTipo(simbs, listaErrores) == "boolean" :
                            return "boolean"
                        else:
                            listaErrores.append("Type error: cannot cond_op two things !boolean")
                            return "typeError"

            if self.lista[0].tipo == '!' :
                if self.lista[1].obtTipo(simbs, listaErrores) == 'boolean' :
                    return "boolean"
                else:
                    listaErrores.append("Cannot ! a thing that is !boolean")
                    return "typeError"

            if self.lista[0].tipo == '(' :
                return self.lista[1].obtTipo(simbs, listaErrores)

        elif self.tipo == 'location' :
            tipoFinal = ""
            for i in simbs[::-1]:
                for j in i:
                    if self.lista[0].nodo.value == j[1]:
                        tipoFinal = j[0]
                        break
            return tipoFinal

        elif self.tipo == 'id' :
            tipoFinal = ""
            for i in simbs[::-1]:
                for j in i:
                    if self.nodo.value == j[1]:
                        tipoFinal = j[0]
                        break
            return tipoFinal

        elif self.tipo == 'literal' :
            if self.lista[0].tipo == "intLiteral" :
                return "int"
            if self.lista[0].tipo == "charLiteral" :
                return "char"
            if self.lista[0].tipo == "stringLiteral" :
                return "string"
            if self.lista[0].tipo == "boolLiteral" :
                return "boolean"
        else:   
            return "default"