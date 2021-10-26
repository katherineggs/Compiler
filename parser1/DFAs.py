
class DFAs:
    # Stacks
    states = [0]
    tokens = ['$']

    gramaticaProgram = [{'<Program>': ['class','Program', '{', '}']}]

    gramatica = [
        {'block': ['{', 'statementList', '}']},                            # bloque de codigo -- {holamundo = ":)" ... }
        {'varDecl': ['type', 'id', ';']},                                  # declarar var tipo identificador -- int n1 
        {'statementList': ['statement']},                                  # linea de codigo
        # --------- Statements -------------
        {'statement': ['if', '(', 'expr', ')', 'block']},                  # if 
        {'statement': ['if', '(', 'expr', ')', 'block', 'else', 'block']}, # if else
        {'statement': ['for', 'id', '=', 'expr', ',', 'expr', 'block']},   # for 
        {'statement': ['return', ';']},                                    # return nada
        {'statement': ['return', 'expr', ';']},                            # return algo
        {'statement': ['break', ';']},                                     # break 
        {'statement': ['continue', ';']},                                  #
        {'statement': ['block']},                                          # block
        {'statement': ['varDecl']},                                        # varDecl
        # --------- Expr -------------
        {'expr': ['literal']}, 
        {'expr': ['-', 'expr']},
        {'expr': ['!', 'expr']},
        {'expr': ['(', 'expr', ')']},
        {'exprList': ['expr']}, 
        # --------- Operators -------------
        {'conditionOperators': ['conditionOperators']},
        {'equalityOperatos': ['equalityOperatos']}, 
        {'operadores': ['operadores']},
        # --------- Literals -------------
        {'literal': ['intLiteral']}, 
        {'literal': ['charLiteral']},
        {'literal': ['boolLiteral']},
        {'stringLiteral': ['stringLiteral']},
        {'charLiteral': ['charLiteral']},
        {'boolLiteral': ['boolLiteral']},
        {'intLiteral': ['intLiteral']}, 
        {'id': ['id']} 
        ]