import abstracts.Symbols as simb
import scanner.TypeSList as sList
import abstracts.Tokens as tk
import scanner.Accepting as Accepting
class Scanner:
    def scanner(self, codigo, debug):
        tokens = []
        errores = []
        for lista in codigo: # codigo - lista de listas
            palabra = lista[0].split(" ") # lista = ["cosas", id]
            for item in palabra:
                id = lista[1]
                error = True

                # si es igual a algun simbolo ya entrcomo token
                if item == "class" : 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[1], id, item))
                    error = False
                elif item == "Program" : 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[2], id, item))
                    error = False

                # Palabras reservadas
                elif item == "boolean" or item == "break" or item == "callout" or item == "continue" or item == "else" or item == "for" or item == "if" or item == "int" or item == "return" or item == "void": 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[3], id, item))
                    error = False

                #  Signos
                elif item == ":" or item == ";" or item == "(" or item == ")" or item == "," or item == "[" or item == "]" or item == "{" or item == "}" or item == "[]" : 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[4], id, item))
                    error = False
                elif item == "!" or item == "$" or item == "%" or item == "&" or item == "*" or item == "+" or item == "." or item == "/" or item == ">" or item == "=" or item == "<" or item == "?" or item == "@" or item == "^" or item == "-" or item == "<=" or item == ">=": 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[5], id, item))
                    error = False

                # Operadores
                elif item == "==" or item == "!=": 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[6], id, item))
                    error = False
                elif item == "=" or item == "+=" or item == "-=": 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[7], id, item))
                    error = False
                elif item == "&&" or item == "||": 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[8], id, item))
                    error = False
                elif item == "true" or item == "false": 
                    tokens.append(tk.Tokens(sList.TypeSList.simbolos[9], id, item))
                    error = False

                # Vemos si nuestro DFA lo acepta como token
                else:
                    dfa = Accepting.Accepting()

                    # Verificamos que si es un string contenga los dos
                    if ('"') in item:
                        if str(item).startswith('"') and str(item).endswith('"'):
                            item = item.replace('"',"")
                            
                    if dfa.accepting("id", item):
                        tokens.append(tk.Tokens(sList.TypeSList.simbolos[10], id, item))
                        error = False
                    if dfa.accepting("int", item):
                        tokens.append(tk.Tokens(sList.TypeSList.simbolos[11], id, item))
                        error = False

                # si error se mantiene True
                if error:
                    errorStr = "Error Lexico: error en la linea " + str(id) + " con el item " + str(item)
                    errores.append(errorStr)
        if debug:
            for token in tokens:
                print(token.prettyPrint())
            for error in errores:
                print("Error -",error)

        return tokens, errores