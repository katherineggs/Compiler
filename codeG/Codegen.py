import abstracts.Symbols as Symbol
import abstracts.Tokens as Token
import abstracts.Node as Node
import abstracts.Program as Program
import parser1.DFAs as ParseDFA
import re
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Codegen:
    def __init__(self):
        self.trueCont = 0
        # self.method_counter_python = 0
        # self.first_method = ""

    def codegen(self, main_program, debug, nombre):
        codeGen = []
        # print(len(main_program.listaIrt))
        for nodo in main_program.listaIrt:
            # print(nodo.instruccion)
            codigo = self.aAssembler(nodo.instruccion, nombre)
            if codigo != None:
                if type(codigo) is list:
                    for codigo_item in codigo:
                        codeGen.append(codigo_item)
                else:
                    codeGen.append(codigo)
        return codeGen
 
    def aAssembler(self, instruccion, nombre):
        print("ASM:", instruccion)
        #analyze instruccion, create new instruccion in ASM
        if instruccion[0] == "INICIOP" :
            l1 = "# " + str(nombre)
            l2 = "# ----------------- variables globales -----------------"
            l3 = ".data"
            l4 = "# ----------------- procedimiento main -----------------"
            l5 = ".text"
            return [l1, l2, l3, l4, l5]
        
        elif instruccion[0] == "ENDP":
            instruccion_list = []
            instruccion_list.append("# Fin de " + nombre)
            instruccion_list.append("jr $ra")

        elif instruccion[0] == "ETIQUETA" :
            l1 = instruccion[1]+":"
            return l1
        
        elif instruccion[0] == "IFCONTI" :
            print("IFCONTI")
            print(instruccion)
            instruccion_list = []
            instruccion_list.append("    # loads data into t1, t0, set s_ to verify ifs")
            if instruccion[3][1]=='==' :
                if instruccion[3][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0])
                if instruccion[3][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][2])
                instruccion_list.append("    seq $s"+str(self.trueCont) + ", $t0, $t1")

            elif instruccion[3][1]=='<' :
                if instruccion[3][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0])
                if instruccion[3][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][2])
                instruccion_list.append("    slt $s"+str(self.trueCont) + ", $t0, $t1")

            elif instruccion[3][1]=='>' :
                if instruccion[3][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0])
                if instruccion[3][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][2])
                instruccion_list.append("    sgt $s"+str(self.trueCont) + ", $t0, $t1")

            elif instruccion[3][1]=='<=' :
                if instruccion[3][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0])
                if instruccion[3][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][2])
                instruccion_list.append("    sle $s"+str(self.trueCont) + ", $t0, $t1")

            elif instruccion[3][1]=='>=' :
                if instruccion[3][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0])
                if instruccion[3][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][2])
                instruccion_list.append("    sge $s"+str(self.trueCont) + ", $t0, $t1")

            elif instruccion[3][1]=='!=' :
                if instruccion[3][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0])
                if instruccion[3][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][2])
                instruccion_list.append("    sne $s"+str(self.trueCont) + ", $t0, $t1")

            elif instruccion[3][1]=='&&' :
                if instruccion[3][0][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0][0])
                if instruccion[3][0][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][0][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][0][2])
                if instruccion[3][0][1] == "==" :
                    instruccion_list.append("    seq $t3, $t0, $t1")
                elif instruccion[3][0][1] == "<" :
                    instruccion_list.append("    slt $t3, $t0, $t1")
                elif instruccion[3][0][1] == ">" :
                    instruccion_list.append("    sgt $t3, $t0, $t1")
                elif instruccion[3][0][1] == "<=" :
                    instruccion_list.append("    sle $t3, $t0, $t1")
                elif instruccion[3][0][1] == ">=" :
                    instruccion_list.append("    sge $t3, $t0, $t1")
                elif instruccion[3][0][1] == "!=" :
                    instruccion_list.append("    sne $t3, $t0, $t1")

                if instruccion[3][2][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t4, " +instruccion[3][2][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t4, " +instruccion[3][2][0])
                if instruccion[3][2][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t5, " +instruccion[3][2][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t5, " +instruccion[3][2][2])
                if instruccion[3][2][1] == "==" :
                    instruccion_list.append("    seq $t6, $t4, $t5")
                elif instruccion[3][2][1] == "<" :
                    instruccion_list.append("    slt $t6, $t4, $t5")
                elif instruccion[3][2][1] == ">" :
                    instruccion_list.append("    sgt $t6, $t4, $t5")
                elif instruccion[3][2][1] == "<=" :
                    instruccion_list.append("    sle $t6, $t4, $t5")
                elif instruccion[3][2][1] == ">=" :
                    instruccion_list.append("    sge $t6, $t4, $t5")
                elif instruccion[3][2][1] == "!=" :
                    instruccion_list.append("    sne $t6, $t4, $t5")

                instruccion_list.append("    and $s"+str(self.trueCont) + ", $t4, $t6")

            elif instruccion[3][1]=='||' :
                if instruccion[3][0][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t0, " +instruccion[3][0][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t0, " +instruccion[3][0][0])
                if instruccion[3][0][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t1, " +instruccion[3][0][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t1, " +instruccion[3][0][2])
                if instruccion[3][0][1] == "==" :
                    instruccion_list.append("    seq $t3, $t0, $t1")
                elif instruccion[3][0][1] == "<" :
                    instruccion_list.append("    slt $t3, $t0, $t1")
                elif instruccion[3][0][1] == ">" :
                    instruccion_list.append("    sgt $t3, $t0, $t1")
                elif instruccion[3][0][1] == "<=" :
                    instruccion_list.append("    sle $t3, $t0, $t1")
                elif instruccion[3][0][1] == ">=" :
                    instruccion_list.append("    sge $t3, $t0, $t1")

                if instruccion[3][2][0][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t4, " +instruccion[3][2][0][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t4, " +instruccion[3][2][0])
                if instruccion[3][2][2][0:4] == "$fp-" :
                    instruccion_list.append("    lw $t5, " +instruccion[3][2][2][4:]+"($fp)")
                else:
                    instruccion_list.append("    li $t5, " +instruccion[3][2][2])
                if instruccion[3][2][1] == "==" :
                    instruccion_list.append("    seq $t6, $t4, $t5")
                elif instruccion[3][2][1] == "<" :
                    instruccion_list.append("    slt $t6, $t4, $t5")
                elif instruccion[3][2][1] == ">" :
                    instruccion_list.append("    sgt $t6, $t4, $t5")
                elif instruccion[3][2][1] == "<=" :
                    instruccion_list.append("    sle $t6, $t4, $t5")
                elif instruccion[3][2][1] == ">=" :
                    instruccion_list.append("    sge $t6, $t4, $t5")

                instruccion_list.append("    or $s"+str(self.trueCont) + ", $t4, $t6")
            #todo && and ||
            # print(self.trueCont)
            self.trueCont+=1
            return instruccion_list
        
        elif(instruccion[0] == "if"):
            instruccion_list = []
            instruccion_list.append("    # jump if condition")
            instruccion_list.append("    li $t0, 1")
            instruccion_list.append("    beq $s"+str(self.trueCont-1) + ", $t0, "+ instruccion[3])
            return instruccion_list
        
        elif(instruccion[0] == "if not"):
            instruccion_list = []
            instruccion_list.append("    # jump if not condition")
            instruccion_list.append("    beq $s"+str(self.trueCont-1) + ", $zero, "+ instruccion[3])
            return instruccion_list
        
        elif(instruccion[0] == "varDecl"):
            instruccion_list = []
            instruccion_list.append("    # var decl, sp=4")
            instruccion_list.append("    addi $sp, $sp, 4")
            return instruccion_list
        
            return instruccion_list

        elif instruccion[0] == "MOVE" :
            if len(instruccion)==4 :
                if type(instruccion[3]) is not list :
                    if instruccion[3][0:4] == "$fp-" :
                        ins4 = "    # moving var2 into var1"
                        l2 = "    lw $t1, "+instruccion[3][4:]+"($fp)"
                        l3 = "    sw $t1, " +instruccion[1][4:]+"($fp)"
                        return [ins4, l2, l3]
                    else:
                        ins4 = "    # load immediate literal into var1"
                        l1 = "    li $t1, "+instruccion[3]
                        l2 = "    sw $t1, "+instruccion[1][4:]+"($fp)"
                        return [ins4, l1, l2]
                elif "&&" in instruccion[3] or "||" in instruccion[3] :
                    l1 = "    # intermidate operetions to var 1 bool"
                    instruccion_list = []
                    instruccion_list.append(l1)

                    if instruccion[3][1]=='&&' :
                        if instruccion[3][0][0][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t0, " +instruccion[3][0][0][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t0, " +instruccion[3][0][0])
                        if instruccion[3][0][2][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t1, " +instruccion[3][0][2][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t1, " +instruccion[3][0][2])
                        if instruccion[3][0][1] == "==" :
                            instruccion_list.append("    seq $t3, $t0, $t1")
                        elif instruccion[3][0][1] == "<" :
                            instruccion_list.append("    slt $t3, $t0, $t1")
                        elif instruccion[3][0][1] == ">" :
                            instruccion_list.append("    sgt $t3, $t0, $t1")
                        elif instruccion[3][0][1] == "<=" :
                            instruccion_list.append("    sle $t3, $t0, $t1")
                        elif instruccion[3][0][1] == ">=" :
                            instruccion_list.append("    sge $t3, $t0, $t1")
                        elif instruccion[3][0][1] == "!=" :
                            instruccion_list.append("    sne $t3, $t0, $t1")

                        if instruccion[3][2][0][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t4, " +instruccion[3][2][0][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t4, " +instruccion[3][2][0])
                        if instruccion[3][2][2][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t5, " +instruccion[3][2][2][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t5, " +instruccion[3][2][2])
                        if instruccion[3][2][1] == "==" :
                            instruccion_list.append("    seq $t6, $t4, $t5")
                        elif instruccion[3][2][1] == "<" :
                            instruccion_list.append("    slt $t6, $t4, $t5")
                        elif instruccion[3][2][1] == ">" :
                            instruccion_list.append("    sgt $t6, $t4, $t5")
                        elif instruccion[3][2][1] == "<=" :
                            instruccion_list.append("    sle $t6, $t4, $t5")
                        elif instruccion[3][2][1] == ">=" :
                            instruccion_list.append("    sge $t6, $t4, $t5")
                        elif instruccion[3][2][1] == "!=" :
                            instruccion_list.append("    sne $t6, $t4, $t5")

                        instruccion_list.append("    and $t1, $t4, $t6")
                        instruccion_list.append("    sw $t1, "+instruccion[1][4:]+"($fp)")
                    elif instruccion[3][1]=='||' :
                        if instruccion[3][0][0][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t0, " +instruccion[3][0][0][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t0, " +instruccion[3][0][0])
                        if instruccion[3][0][2][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t1, " +instruccion[3][0][2][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t1, " +instruccion[3][0][2])
                        if instruccion[3][0][1] == "==" :
                            instruccion_list.append("    seq $t3, $t0, $t1")
                        elif instruccion[3][0][1] == "<" :
                            instruccion_list.append("    slt $t3, $t0, $t1")
                        elif instruccion[3][0][1] == ">" :
                            instruccion_list.append("    sgt $t3, $t0, $t1")
                        elif instruccion[3][0][1] == "<=" :
                            instruccion_list.append("    sle $t3, $t0, $t1")
                        elif instruccion[3][0][1] == ">=" :
                            instruccion_list.append("    sge $t3, $t0, $t1")

                        if instruccion[3][2][0][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t4, " +instruccion[3][2][0][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t4, " +instruccion[3][2][0])
                        if instruccion[3][2][2][0:4] == "$fp-" :
                            instruccion_list.append("    lw $t5, " +instruccion[3][2][2][4:]+"($fp)")
                        else:
                            instruccion_list.append("    li $t5, " +instruccion[3][2][2])
                        if instruccion[3][2][1] == "==" :
                            instruccion_list.append("    seq $t6, $t4, $t5")
                        elif instruccion[3][2][1] == "<" :
                            instruccion_list.append("    slt $t6, $t4, $t5")
                        elif instruccion[3][2][1] == ">" :
                            instruccion_list.append("    sgt $t6, $t4, $t5")
                        elif instruccion[3][2][1] == "<=" :
                            instruccion_list.append("    sle $t6, $t4, $t5")
                        elif instruccion[3][2][1] == ">=" :
                            instruccion_list.append("    sge $t6, $t4, $t5")

                        instruccion_list.append("    or $t1, $t4, $t6")
                        instruccion_list.append("    sw $t1, "+instruccion[1][4:]+"($fp)")
                    return instruccion_list

                else:
                    l1 = "    # intermidate operetions to var 1"
                    instruccion_list = []
                    instruccion_list.append(l1)

                    temp_instruccion_list = []

                    temp_instruccion_list.append("    sw $t9, " +instruccion[1][4:]+"($fp)")
                    deep_level = 9
                    current_list = instruccion[3]
                    while deep_level>=0 and (type(current_list) is list) :
                        # print(current_list, deep_level)
                        if current_list[1] == '+' :
                            #add save, s1, s2
                            temp_instruccion_list.append("    add $t"+str(deep_level) +", $t"+str(deep_level-1) + ", $t0")
                            if current_list[2][0:4] == "$fp-" :
                                temp_instruccion_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruccion_list.append("    li $t0, " +current_list[2])
                            if type(current_list[0]) is not list :
                                if current_list[0][0:4] == "$fp-" :
                                    temp_instruccion_list.append("    lw $t"+ str(deep_level-1) +", " +current_list[0][4:]+"($fp)")
                                else:
                                    temp_instruccion_list.append("    li $t"+ str(deep_level-1) +", " +current_list[0])
                        elif current_list[1] == '-' :
                            #sub save, r1, r2
                            temp_instruccion_list.append("    sub $t"+str(deep_level) +", $t"+str(deep_level-1) + ", $t0")
                            if current_list[2][0:4] == "$fp-" :
                                temp_instruccion_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruccion_list.append("    li $t0, " +current_list[2])
                            if type(current_list[0]) is not list :
                                if current_list[0][0:4] == "$fp-" :
                                    temp_instruccion_list.append("    lw $t"+ str(deep_level-2) +", " +current_list[2][4:]+"($fp)")
                                else:
                                    temp_instruccion_list.append("    li $t"+ str(deep_level-2) +", " +current_list[2])
                        elif current_list[1] == '*' :
                            #mul save, m1, m2
                            temp_instruccion_list.append("    mul $t"+str(deep_level) +", $t"+str(deep_level-1) + ", $t0")
                            if current_list[2][0:4] == "$fp-" :
                                temp_instruccion_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruccion_list.append("    li $t0, " +current_list[2])
                            if type(current_list[0]) is not list :
                                if current_list[0][0:4] == "$fp-" :
                                    temp_instruccion_list.append("    lw $t"+ str(deep_level-2) +", " +current_list[2][4:]+"($fp)")
                                else:
                                    temp_instruccion_list.append("    li $t"+ str(deep_level-2) +", " +current_list[2])
                        elif current_list[1] == '/' :
                            #div d1/d2
                            #sw lo save
                            temp_instruccion_list.append("    move $t"+str(deep_level) + ", mflo")
                            temp_instruccion_list.append("    div $t"+str(deep_level-1) + ", $t0")
                            if current_list[2][0:4] == "$fp-" :
                                temp_instruccion_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruccion_list.append("    li $t0, " +current_list[2])
                            if type(current_list[0]) is not list :
                                if current_list[0][0:4] == "$fp-" :
                                    temp_instruccion_list.append("    lw $t"+ str(deep_level-2) +", " +current_list[2][4:]+"($fp)")
                                else:
                                    temp_instruccion_list.append("    li $t"+ str(deep_level-2) +", " +current_list[2])
                        current_list = current_list[0]
                        deep_level-=1

                    for temp_instruccion in temp_instruccion_list[::-1]:
                        instruccion_list.append(temp_instruccion)
                    return instruccion_list
       
        elif instruccion[0] == "SUM" :
            if instruccion[3][0:4] == "$fp-" :
                l1 = "    # sums var1 + var2, saves in var1"
                l2 = "    lw $t0, "+instruccion[1][4:]+"($fp)"
                l3 = "    lw $t1, "+instruccion[3][4:]+"($fp)"
                ins4 = "    add $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruccion[1][4:]+"($fp)"
                return [l1, l2, l3, ins4, ins5]
            else:
                l1 = "    # sums var1 + immediate, saves in var1"
                l2 = "    lw $t0, "+instruccion[1][4:]+"($fp)"
                l3 = "    li $t1, "+instruccion[3]
                ins4 = "    add $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruccion[1][4:]+"($fp)"
                return [l1, l2, l3, ins4, ins5]                
       
        elif instruccion[0] == "MINUS" :
            if instruccion[3][0:4] == "$fp-" :
                l1 = "    # subs var1 + var2, saves in var1"
                l2 = "    lw $t0, "+instruccion[1][4:]+"($fp)"
                l3 = "    lw $t1, "+instruccion[3][4:]+"($fp)"
                ins4 = "    sub $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruccion[1][4:]+"($fp)"
                return [l1, l2, l3, ins4, ins5]
            else:
                l1 = "    # subs var1 + immediate, saves in var1"
                l2 = "    lw $t0, "+instruccion[1][4:]+"($fp)"
                l3 = "    li $t1, "+instruccion[3]
                ins4 = "    sub $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruccion[1][4:]+"($fp)"
                return [l1, l2, l3, ins4, ins5]

