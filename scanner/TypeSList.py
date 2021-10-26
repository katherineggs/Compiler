import abstracts.Symbols as simb

class TypeSList:
    # Los simbolos los vamos a declarar
    simbolos =[]

    # simbolos.append(simb.Symbol(id, reggex, "nombre"))
    # separamos class program por como leemos el input
    simbolos.append(simb.Symbol(1,"class", "<class>"))
    simbolos.append(simb.Symbol(2,"Program", "<Program>"))
    # Palabras Reservadas
    simbolos.append(simb.Symbol(3,"break|callout|continue|else|for|if|return|void", "<reservedW>"))
    # Signos
    simbolos.append(simb.Symbol(4,":|;|(|)|,|[|]|{|}|[]", "<signos>"))
    simbolos.append(simb.Symbol(5,"<|>|<=|>=|+|-|*|/|%", "<operadores>"))

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
    
    simbolos.append(simb.Symbol(15, "boolean|int", "<type>"))
    