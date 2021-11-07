from anytree import Node as nodeImp

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
                nodoAnyT = nodeImp(nodoL.tipo + ' ' + str(cont), parent = nodoPrinc)
                Program.append(nodoL.tipo + ' ' + str(cont))
                cont += 1
                if len(nodoL.lista) != 0 :
                    cont = nodoL.obtNodos(Program, cont, nodoAnyT)
        return cont
    
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

    def checkTipo(self, simbs, cont, listaErrores):
        print(simbs, cont, listaErrores)


    #------------------------------------------------------------------------- Semantic
    def analisisSemantico(self, simbs, cont, listaErrores, puntero):
        if(len(self.lista)!=0 and self.tipo!=''):
            cont2 = 0
            for node1 in self.lista:
                # print(type(node1.nodo))
                if(len(node1.lista)==0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.name=="id"):
                    if(cont2!=0 and (self.lista[cont2-1].nodo.tipoSimbolo.name == 'type' or self.lista[cont2-1].nodo.tipoSimbolo.name == 'void')):
                        unico = True
                        for verificarSimbolo in simbs[-1]:
                            if node1.nodo.value == verificarSimbolo[1]:
                                unico = False
                        if(unico):
                            puntero += 4
                            simbs[-1].append([self.lista[cont2-1].nodo.value, node1.nodo.value, node1.nodo.line, "$fp-" + str(puntero)])
                        else:
                            listaErrores.append("Semantic error, Uniqueness check: este identificador ya se usa en la línea " + str(node1.nodo.line))
                    else:
                        is_decl = False
                        for decls in simbs[::-1]:
                            for decl in decls:
                                if node1.nodo.value == decl[1]:
                                    is_decl = True
                        if not(is_decl):
                            listaErrores.append("Semantic error, Uniqueness check: Var not declared in line "+str(node1.nodo.line))
                
                if(len(node1.lista)==0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.name=="("):
                    if(cont2!=0 and cont2!=1):
                        if(self.lista[cont2-1].nodo.tipoSimbolo.name == 'id' and 
                            (self.lista[cont2-2].nodo.tipoSimbolo.name == 'void' or self.lista[cont2-2].nodo.tipoSimbolo.name == 'type')):
                            simbs.append([])

                if(len(node1.lista)==0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.name=="{"):
                    simbs.append([])

                if(len(node1.lista)==0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.name=="}"):
                    pass
                    # print("pop scope")
                    #del main_program.simbs[-1]

                if(node1.tipo == "expr"):
                    if(len(node1.lista) > 0):
                        if(node1.lista[0].tipo == 'expr'):
                            if(node1.lista[1].tipo == 'bin_op'):

                                #---- NO TENEMOS ESTAS -------????????????????????????????
                                if(node1.lista[1].lista[0].tipo == 'arit_op'):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "int" and type_exp2!="int"):
                                        listaErrores.append("Type error: cannot arit op two !ints")

                                if(node1.lista[1].lista[0].tipo == 'rel_op'):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "int" and type_exp2!="int"):
                                        listaErrores.append("Type error: cannot rel op two !ints")

                                if(node1.lista[1].lista[0].tipo == 'eq_op'):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != type_exp2):
                                        listaErrores.append("Type error: cannot eq op two things with diff type")

                                if(node1.lista[1].lista[0].tipo == 'cond_op'):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "boolean" and type_exp2!="boolean"):
                                        listaErrores.append("Type error: cannot cond op two things !boolean")

                            elif(node1.lista[1].tipo == 'minus_op'):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "int" and type_exp2!="int"):
                                        listaErrores.append("Type error: cannot minus op two !ints")

                        if(node1.lista[0].tipo == 'minus_op'):
                            type_exp = node1.lista[1].obtTipo(simbs, listaErrores)
                            if(type_exp != "type_error" and type_exp!="int"):
                                listaErrores.append("Type error: cannot minus op a thing that is !int")

                        if(node1.lista[0].tipo == '!'):
                            type_exp = node1.lista[1].obtTipo(simbs, listaErrores)
                            if(type_exp != "type_error" and type_exp!="boolean"):
                                listaErrores.append("Type error: cannot ! op a thing that is !boolean")

                        #---- NO TENEMOS ESTAS -------????????????????????????????

                if(node1.tipo == "statement"):
                    if(len(node1.lista) > 0):
                        if(node1.lista[0].tipo == 'if'):
                            type_exp = node1.lista[2].obtTipo(simbs, listaErrores)
                            if(type_exp != "type_error" and type_exp != "boolean"):
                                listaErrores.append("Type error: cannot IF without boolean")

                        if(node1.lista[0].tipo == 'for'):
                            type_exp_1 = node1.lista[3].obtTipo(simbs, listaErrores)
                            type_exp_2 = node1.lista[5].obtTipo(simbs, listaErrores)
                            type_id = node1.lista[1].obtTipo(simbs, listaErrores)

                            if(type_exp_2 != "type_error" and type_exp_2 != "boolean"):
                                listaErrores.append("Type error: cannot FOR without boolean")

                            if(type_exp_1 != "type_error" and type_exp_1 != "int"):
                                listaErrores.append("Type error: cannot FOR without int decl")

                            if(type_id != "type_error" and type_id != "int"):
                                listaErrores.append("Type error: cannot FOR without id int decl")
                            
                        if(node1.lista[0].tipo == 'location'):
                            location_type = ""
                            type_1 = node1.lista[0].obtTipo(simbs, listaErrores)
                            type_2 = node1.lista[2].obtTipo(simbs, listaErrores)

                            if(type_1 != type_2 and (type_1 != "type_error" and type_2 != "type_error")):
                                listaErrores.append("Type error: cannot assign " + 
                                node1.lista[2].obtTipo(simbs, listaErrores) + " in "
                                + node1.lista[0].obtTipo(simbs, listaErrores))

                cont+=1
                cont2+=1
                if(len(node1.lista)!=0):
                    cont = node1.analisisSemantico(simbs, cont, listaErrores, puntero)
        return cont