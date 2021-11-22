from anytree import Node as nodeImp
from scanner.TypeSList import TypeSList
import abstracts.IrtNode as IrtNode

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
            # print("\nSELF")
            # print(self.lista[0].tipo)
            if self.lista[0].tipo == 'location' :
                tipoFinal = ""
                for i in simbs[::-1]:
                    for j in i:
                        if self.lista[0].lista[0].nodo.value == j[1]:
                            tipoFinal = j[0]
                            break
                return tipoFinal

            if self.lista[0].tipo == 'methodCall' :
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
                    if self.lista[1].lista[0].tipo == "+|-|*|/|%": #arith
                        if self.lista[0].obtTipo(simbs, listaErrores) == "int" and self.lista[2].obtTipo(simbs, listaErrores) == "int":
                            return "int"
                        else:
                            listaErrores.append("Type error: No se pueden operar dos ints diferentes")
                            return "typeError"

                    if self.lista[1].lista[0].tipo in "<|>|<=|>=" : # relation
                        if self.lista[0].obtTipo(simbs, listaErrores) == "int" and self.lista[2].obtTipo(simbs, listaErrores) == "int":
                            return "boolean"
                        else:
                            listaErrores.append("Type error: No se pueden operar dos elementos que no sean int")
                            return "typeError"

                    if self.lista[1].lista[0].tipo  in TypeSList.simbolos[5].regEx : # eq
                        if self.lista[0].obtTipo(simbs, listaErrores) == self.lista[2].obtTipo(simbs, listaErrores) :
                            return "boolean"
                        else:
                            listaErrores.append("Type error: No se pueden operar diferentes tipos")
                            return "typeError"

                    if self.lista[1].lista[0].tipo  in TypeSList.simbolos[7].regEx : #cond
                        if self.lista[0].obtTipo(simbs, listaErrores) == "boolean" and self.lista[2].obtTipo(simbs, listaErrores) == "boolean" :
                            return "boolean"
                        else:
                            listaErrores.append("Type error: No se pueden operar dos boolean diferentes")
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
        fieldDeclTipo = []
        if(len(self.lista)!=0 and self.tipo!=''):
            cont2 = 0
            for node1 in self.lista:
                # print(node1.lista)
                # print(type(node1))
                if(len(node1.lista) == 0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.nommbre == "<id>"):
                    if(cont2!=0 and (self.lista[cont2-1].nodo.tipoSimbolo.nommbre == '<type>' or self.lista[cont2-1].nodo.value == 'void')):
                        # Uniqueness check
                        unico = True
                        for verificarSimbolo in simbs[-1]:
                            #print("verificar sim", verificarSimbolo)
                            if node1.nodo.value == verificarSimbolo[1]:
                                unico = False
                        if(unico):
                            puntero += 4
                            simbs[-1].append([self.lista[cont2-1].nodo.value, node1.nodo.value, node1.nodo.id, "$fp-" + str(puntero)])
                        else:
                            listaErrores.append("Error Semántico, Uniqueness check: este identificador ya se usa en la línea " + str(node1.nodo.id))
                    else:
                        is_decl = False
                        for decls in simbs[::-1]:
                            for decl in decls:
                                if node1.nodo.value == decl[1]:
                                    is_decl = True
                        if not(is_decl):
                            listaErrores.append("Error Semántico, Uniqueness check: Variable no declarada en la línea "+str(node1.nodo.id))
                
                if(len(node1.lista) == 0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.nommbre == "("):
                    if(cont2 != 0 and cont2 != 1):
                        # if es una funcion
                        if(self.lista[cont2-1].nodo.tipoSimbolo.nommbre == '<id>' and 
                            (self.lista[cont2-2].nodo.tipoSimbolo.value == 'void' or self.lista[cont2-2].nodo.tipoSimbolo.nommbre == '<type>')):
                            simbs.append([])

                if(len(node1.lista) == 0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.nommbre == "{"):
                    simbs.append([])

                if(len(node1.lista) == 0 and str(type(node1.nodo)) == "<class 'abstracts.Tokens.Tokens'>" and node1.nodo.tipoSimbolo.nommbre == "}"):
                    pass

                if(node1.tipo == "expr"):
                    if(len(node1.lista) > 0):
                        if(node1.lista[0].tipo == 'expr'):
                            if(node1.lista[1].tipo == 'binOp'):
                                if(node1.lista[1].lista[0].tipo in TypeSList.simbolos[4].regEx ):
                                    # print("listaaaaaaa")
                                    # print(node1.lista[1].lista)
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "typeError" and type_exp2!="typeError" and type_exp1 != "int" and type_exp2!="int"):
                                        listaErrores.append("Type Error: No se pueden operar dos ints diferentes")

                                if(node1.lista[1].lista[0].tipo in TypeSList.simbolos[5].regEx ):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "typeError" and type_exp2!="typeError" and type_exp1 != type_exp2):
                                        listaErrores.append("Type error: No se pueden operar diferentes tipos")

                                if(node1.lista[1].lista[0].tipo in TypeSList.simbolos[7].regEx ):
                                    type_exp1 = node1.lista[0].obtTipo(simbs, listaErrores)
                                    type_exp2 = node1.lista[2].obtTipo(simbs, listaErrores)
                                    if(type_exp1 != "typeError" and type_exp2!="typeError" and type_exp1 != "boolean" and type_exp2!="boolean"):
                                        listaErrores.append("Type error: No se pueden operar dos boolean diferentes")

                if(node1.tipo == "statement"):
                    #print("statement")
                    if(len(node1.lista) > 0):
                        if(node1.lista[0].tipo == 'if'):
                            print("-- symbol table")
                            print(simbs)

                            for tipo in simbs:
                                fieldDeclTipo.append(tipo[0][0])

                            # print("\n--- tipo")
                            # print(fieldDeclTipo)

                            type_exp = node1.lista[2].obtTipo(simbs, listaErrores)
                            # print("\n-- Type exp: ", type_exp)

                            if(type_exp != "typeError" and type_exp != "boolean"):
                                listaErrores.append("Type error: if sin condición boolean")

                        if(node1.lista[0].tipo == 'for'):
                            type_exp_1 = node1.lista[3].obtTipo(simbs, listaErrores)
                            type_exp_2 = node1.lista[5].obtTipo(simbs, listaErrores)
                            type_id = node1.lista[1].obtTipo(simbs, listaErrores)

                            if(type_exp_2 != "typeError" and type_exp_2 != "boolean"):
                                listaErrores.append("Type error: for sin condición boolean")

                            if(type_exp_1 != "typeError" and type_exp_1 != "int"):
                                listaErrores.append("Type error: int no declarado dentro de for")

                            if(type_id != "typeError" and type_id != "int"):
                                listaErrores.append("Type error: id int no declarado detro de for")
                            
                        if(node1.lista[0].tipo == 'location'):
                            locationtype = ""
                            type_1 = node1.lista[0].obtTipo(simbs, listaErrores)
                            type_2 = node1.lista[2].obtTipo(simbs, listaErrores)

                            if(type_1 != type_2 and (type_1 != "typeError" and type_2 != "typeError")):
                                listaErrores.append("Type error: No se puede asignar " + node1.lista[2].obtTipo(simbs, listaErrores) + " in " + node1.lista[0].obtTipo(simbs, listaErrores))

                cont+=1
                cont2+=1
                if(len(node1.lista)!=0):
                    cont = node1.analisisSemantico(simbs, cont, listaErrores, puntero)
        return cont


# ------------------------------------------------------------------------- IRT
    def obtIrtInstructions(self, listaIrt, simbs, cont, etiq=""):
        cont += 1
        if(self.tipo == "fieldList"):
            for vari in self.lista:
                cont = vari.obtIrtInstructions(listaIrt, simbs, cont)
        if(self.tipo == "listaMethod"):
            for methodi in self.lista:
                cont = methodi.obtIrtInstructions(listaIrt, simbs, cont)
        if(self.tipo == "fieldDecl"):
            listaIrt.append(IrtNode.IrtNode(self.tipo, [str(cont) + " Instrucciones: " + self.tipo]))
        if(self.tipo == "methodDecl"):
            listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA", self.lista[1].nodo.value]))
            listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["IniciaMethod"]))
            if(len(self.lista[3].lista) != 0):
                cont = self.lista[3].obtIrtInstructions(listaIrt, simbs, cont)
            cont = self.lista[5].obtIrtInstructions(listaIrt, simbs, cont)
            listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinMethod"]))
            # listaIrt.append(IrtNode.IrtNode(self.tipo, str(cont) + "Instrucciones: " + self.tipo))
        # return ""
        if(self.tipo == "block"):
            listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["IniciaBlock"]))

            if(len(self.lista[1].lista) != 0):
                for stati in self.lista[1].lista:
                    cont = stati.obtIrtInstructions(listaIrt, simbs, cont)

            listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinBlock"]))

        if(self.tipo == "statement"):
            cont+=1
            listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["IniciaStatement"]))
            listaIrt.append(IrtNode.IrtNode(self.tipo, [str(cont) + " Instrucciones: " + self.tipo]))
            #if is if -->
            if(self.lista[0].tipo == "varDecl"):
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["varDecl"]))
            elif(self.lista[0].tipo == "if" and len(self.lista) == 5):
                labelExpr = "T" + str(cont)
                etiq = "L"+str(cont)
                etiqSeguir = "L"+str(cont+1)
                cont = self.lista[2].obtIrtInstructions(listaIrt, simbs, cont, labelExpr)
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if", labelExpr, "Goto", etiq]))
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if not", labelExpr, "Goto",etiqSeguir]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA", etiq]))
                cont = self.lista[4].obtIrtInstructions(listaIrt, simbs, cont)
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["Goto",etiqSeguir]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinStatement"]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA",etiqSeguir])) 
            elif(self.lista[0].tipo == "if" and len(self.lista)==7):
                labelExpr = "T"+str(cont)
                etiq = "L"+str(cont)
                elseE = "L"+str(cont+1)
                etiqSeguir = "L"+str(cont+2)
                cont = self.lista[2].obtIrtInstructions(listaIrt, simbs, cont, labelExpr)
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if", labelExpr, "Goto",etiq]))
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if not", labelExpr, "Goto",elseE]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA",etiq]))
                cont = self.lista[4].obtIrtInstructions(listaIrt, simbs, cont)
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["Goto", etiqSeguir]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA",elseE])) 
                cont = self.lista[6].obtIrtInstructions(listaIrt, simbs, cont)
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["Goto", etiqSeguir]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinStatement"]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA",etiqSeguir])) 
            elif(self.lista[0].tipo == "for"):
                operadores = self.lista[2].valorMin(simbs, cont) 
                if(operadores == "="):
                    listaIrt.append(IrtNode.IrtNode(self.tipo,
                        ["MOVE",self.lista[1].valorMin(simbs, cont),
                        operadores, self.lista[3].valorMin(simbs, cont) ]))
                elif(operadores == "+="):
                    listaIrt.append(IrtNode.IrtNode(self.tipo, 
                        ["SUM", self.lista[1].valorMin(simbs, cont),
                        self.lista[1].valorMin(simbs, cont),
                        self.lista[3].valorMin(simbs, cont) ]))
                elif(operadores == "-="):
                    listaIrt.append(IrtNode.IrtNode(self.tipo, 
                        ["MINUS", self.lista[1].valorMin(simbs, cont),
                        self.lista[1].valorMin(simbs, cont),
                        self.lista[3].valorMin(simbs, cont) ]))

                labelExpr = "T"+str(cont)
                etiq = "L"+str(cont)
                etiqSeguir = "L"+str(cont+1)
                cont = self.lista[5].obtIrtInstructions(listaIrt, simbs, cont, labelExpr)
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if",labelExpr,"Goto",etiq]))
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if not", labelExpr, "Goto",etiqSeguir]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA", etiq]))
                cont = self.lista[6].obtIrtInstructions(listaIrt, simbs, cont)
                cont = self.lista[5].obtIrtInstructions(listaIrt, simbs, cont, labelExpr)
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if",labelExpr,"Goto",etiq]))
                listaIrt.append(IrtNode.IrtNode(self.tipo, ["if not", labelExpr, "Goto",etiqSeguir]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinStatement"]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["ETIQUETA",etiqSeguir])) 
            elif(self.lista[0].tipo == "location" and len(self.lista)==4): 
                operadores = self.lista[1].valorMin(simbs, cont) 
                if(operadores == "="):
                    listaIrt.append(IrtNode.IrtNode(self.tipo,
                        ["MOVE",self.lista[0].valorMin(simbs, cont),
                        operadores, self.lista[2].valorMin(simbs, cont) ]))
                elif(operadores == "+="):
                    listaIrt.append(IrtNode.IrtNode(self.tipo, 
                        ["SUM", self.lista[0].valorMin(simbs, cont),
                        self.lista[0].valorMin(simbs, cont),
                        self.lista[2].valorMin(simbs, cont) ]))
                elif(operadores == "-="):
                    listaIrt.append(IrtNode.IrtNode(self.tipo, 
                        ["MINUS", self.lista[0].valorMin(simbs, cont),
                        self.lista[0].valorMin(simbs, cont),
                        self.lista[2].valorMin(simbs, cont) ]))
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinStatement"]))
            else:
                listaIrt.append(IrtNode.IrtNode(self.tipo + str(cont), ["FinStatement"]))
            #vard_decl -->

            #for --> 

            #location;assign;expr -->

            #methodcall -->

            #return;break;continue

            #block -->
            
        if(self.tipo == "expr"):
            cont+=1
            listaIrt.append(IrtNode.IrtNode(self.tipo, [str(cont) + " Instrucciones: " + self.tipo]))
            #expr binop expr 
            #expr.getValue ; binop getValue ; expr get value
            if(len(self.lista) == 3):
                if(self.lista[0].tipo == "expr" and 
                    self.lista[1].tipo=="bin_op" and 
                    self.lista[2].tipo=="expr"):
                    if(len(self.lista[0].lista)==1 and len(self.lista[1].lista)==1 and len(self.lista[1].lista)==1 ):
                        instruction = [self.lista[0].valorMin(simbs, cont), self.lista[1].valorMin(simbs, cont), self.lista[2].valorMin(simbs, cont)]
                        if(etiq!=""):
                            listaIrt.append(IrtNode.IrtNode(self.tipo, ["IF_BOOL",etiq,"=",instruction]))
                        else:
                            listaIrt.append(IrtNode.IrtNode(self.tipo, ["IF_BOOL","T"+ str(cont),"=",instruction]))
                    else:
                        instruction = [self.lista[0].valorMin(simbs, cont), self.lista[1].valorMin(simbs, cont), self.lista[2].valorMin(simbs, cont)]
                        if(etiq!=""):
                            listaIrt.append(IrtNode.IrtNode(self.tipo, ["IF_BOOL",etiq,"=",instruction]))
                        else:
                            listaIrt.append(IrtNode.IrtNode(self.tipo, ["IF_BOOL","T"+ str(cont),"=",instruction]))
                elif(self.lista[0].tipo == "expr" and 
                    self.lista[1].tipo=="minus_op" and 
                    self.lista[2].tipo=="expr"):
                    if(len(self.lista[0].lista)==1 and len(self.lista[1].lista)==1 ):
                        instruction = [self.lista[0].valorMin(simbs, cont), self.lista[1].valorMin(simbs, cont), self.lista[2].valorMin(simbs, cont)]
                        if(etiq!=""):
                            listaIrt.append(IrtNode.IrtNode(self.tipo, ["IF_BOOL",etiq,"=",instruction]))
                        else:
                            listaIrt.append(IrtNode.IrtNode(self.tipo, ["IF_BOOL","T"+ str(cont),"=",instruction]))
                
                elif(self.lista[0].tipo=="("):
                    self.lista[1].obtIrtInstructions(listaIrt, simbs, cont, etiq)
            elif(self.lista[0].tipo=="("):
                self.lista[1].obtIrtInstructions(listaIrt, simbs, cont, etiq)
            #suma -- >
            #compare -- >
            #method call -- >
        return cont

    def getNodesIrt(self, listaIrt, simbs, cont):
        if(len(self.lista)!=0 and self.tipo!=''):
            for node1 in self.lista:
                node1.obtIrtInstructions(listaIrt, simbs, cont)
                cont+=1
                if(len(node1.lista)!=0):
                    cont = node1.getNodesIrt(listaIrt, simbs, cont)
        return cont
