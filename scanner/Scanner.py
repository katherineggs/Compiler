import abstracts.Symbols as simb
import abstracts.Tokens as tk
import scanner.Accepting as Accepting
class Scanner:

    # Los simbolos los vamos a declarar
    simbolos =[]

    # simbolos.append(simb.Symbol(id, reggex, "nombre"))
    # separamos class program por como leemos el input
    simbolos.append(simb.Symbol(1,"class", "<class>"))
    simbolos.append(simb.Symbol(2,"Program", "<Program>"))
    # Palabras Reservadas
    simbolos.append(simb.Symbol(3,"boolean|break|callout|continue|else|for|if|int|return|void", "<reservedW>"))
    # Signos
    simbolos.append(simb.Symbol(4,":|;|(|)|,|[|]|{|}|[]", "<signos>"))
    simbolos.append(simb.Symbol(5,"!|$|%|&|*|+|.|/|>|=|<|?|@|\|^|-|<=|>=", "<operadores>"))
    # operadores
    simbolos.append(simb.Symbol(6,"==|!=", "<equalityOperatos>"))
    simbolos.append(simb.Symbol(7,"=|+=|-=", "<assignOperators>"))
    simbolos.append(simb.Symbol(8,"&&|||", "<conditionOperators>"))
    simbolos.append(simb.Symbol(9, "true|false", "<boolLiteral>"))
    # Estos los comparamos con las palabras 
    simbolos.append(simb.Symbol(10,"", "<id>"))
    simbolos.append(simb.Symbol(11,"", "<intLiteral>"))
    simbolos.append(simb.Symbol(12,"", "<stringLiteral>"))
    simbolos.append(simb.Symbol(13,"", "<charLiteral>"))
    simbolos.append(simb.Symbol(14,"", "<Token no valido>"))

    def scanner(self, codigo, debug):
        tokens = []
        prettyTokens = []
        errores = []
        # bonitos = simb.__()
        # print("bonitos", self.simbolos[13])
        for lista in codigo: # codigo - lista de listas
            palabra = lista[0].split(" ") # lista = ["cosas", id]
            for item in palabra:
                id = lista[1]
                error = True

                # si es igual a algun simbolo ya entrcomo token
                if item == "class" : 
                    prettyTokens.append(tk.Tokens(self.simbolos[1], id, item))
                    tokens.append(tk.Tokens(self.simbolos[1], id, item))
                    error = False
                elif item == "Program" : 
                    tokens.append(tk.Tokens(self.simbolos[2], id, item))
                    error = False

                # Palabras reservadas
                elif item == "boolean" or item == "break" or item == "callout" or item == "continue" or item == "else" or item == "for" or item == "if" or item == "int" or item == "return" or item == "void": 
                    tokens.append(tk.Tokens(self.simbolos[3], id, item))
                    error = False

                #  Signos
                elif item == ":" or item == ";" or item == "(" or item == ")" or item == "," or item == "[" or item == "]" or item == "{" or item == "}" or item == "[]" : 
                    tokens.append(tk.Tokens(self.simbolos[4], id, item))
                    error = False
                elif item == "!" or item == "$" or item == "%" or item == "&" or item == "*" or item == "+" or item == "." or item == "/" or item == ">" or item == "=" or item == "<" or item == "?" or item == "@" or item == "^" or item == "-" or item == "<=" or item == ">=": 
                    tokens.append(tk.Tokens(self.simbolos[5], id, item))
                    error = False

                # Operadores
                elif item == "==" or item == "!=": 
                    tokens.append(tk.Tokens(self.simbolos[6], id, item))
                    error = False
                elif item == "=" or item == "+=" or item == "-=": 
                    tokens.append(tk.Tokens(self.simbolos[7], id, item))
                    error = False
                elif item == "&&" or item == "||": 
                    tokens.append(tk.Tokens(self.simbolos[8], id, item))
                    error = False
                elif item == "true" or item == "false": 
                    tokens.append(tk.Tokens(self.simbolos[9], id, item))
                    error = False

                # Vemos si nuestro DFA lo acepta como token
                else:
                    dfa = Accepting.Accepting()

                    if (dfa.accepting("id", item)):
                        tokens.append(tk.Tokens(self.simbolos[10], id, item))
                        error = False
                    if (dfa.accepting("int", item)):
                        tokens.append(tk.Tokens(self.simbolos[11], id, item))
                        error = False

                # si error se mantiene True
                if error:
                    errorStr = "Error Lexico: error en la linea " + str(id)
                    errores.append(errorStr)
        if debug:
            for token in tokens:
                print(token.prettyPrint())
            for error in errores:
                print(error)

        return tokens, errores