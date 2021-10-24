import abstracts.Node as nodoA
import abstracts.FieldDecl as field
import abstracts.MethodDecl as metodo
import abstracts.VarDeclList as listaVariables
import abstracts.Block as block

class DFAs:
    # Stacks
    states = [0]

    tokens = ['$']

    gramaticaProgram = [{'<Program>': ['class','Program', '{', '}']}]

    dfaProgram = {
        0:{'class':['shift', 1], '<program>':['goTo', 5]},
        1:{'Program':['shift', 2]},
        2:{'{':['shift', 3]},
        3:{'}':['shift', 4]},
        4:{'}':['reduce', 1]},
        5: {'$': ['accept', 2]} }

    gramatica = [
        {'block': ['{', 'statementList', '}']},
        {'statementList': ['statement']}, {'statementList': ['statement', 'statementList']},
        {'varDecl': ['type', 'id', ';']},
        {'statement': ['location', 'assignOperators', 'expr', ';']}, 
        {'statement': ['methodCall', ';']}, 
        {'statement': ['if', '(', 'expr', ')', 'block']},
        {'statement': ['if', '(', 'expr', ')', 'block', 'else', 'block']},
        {'statement': ['for', 'id', '=', 'expr', ',', 'expr', 'block']}, 
        {'statement': ['return', ';']},
        {'statement': ['return', 'expr', ';']},  
        {'statement': ['break', ';']},
        {'statement': ['continue', ';']}, 
        {'statement': ['block']},
        {'statement': ['varDecl']},
        {'expr': ['location']}, 
        {'expr': ['methodCall']},
        {'expr': ['literal']}, 
        {'expr': ['expr', 'binOp', 'expr']}, 
        {'expr': ['-', 'expr']},
        {'expr': ['!', 'expr']},
        {'expr': ['(', 'expr', ')']},
        {'location': ['id']},
        {'location': ['id', '[', 'expr', ']']},
        {'methodName': ['id']}, 
        {'methodCall': ['methodName', '(', ')']}, 
        {'methodCall': ['methodName', '(', 'exprList', ')']}, 
        {'methodCall': ['callout', '(', 'stringLiteral', ')']},
        {'methodCall': ['callout', '(', 'stringLiteral', ',', 'calloutArgsL', ')']}, 
        {'calloutArgsL': ['argCallout']},
        {'calloutArgsL': ['argCallout', 'calloutArgsL']}, 
        {'exprList': ['expr']}, 
        {'exprList': ['expr',',', 'exprList']},
        {'argCallout': ['expr']},
        {'argCallout': ['stringLiteral']}, 
        {'binOp': ['operadores']},
        {'binOp': ['equalityOperatos']},
        {'binOp': ['conditionOperators']},
        {'conditionOperators': ['conditionOperators']},
        {'equalityOperatos': ['equalityOperatos']}, 
        {'operadores': ['operadores']},
        {'literal': ['intLiteral']}, 
        {'literal': ['charLiteral']},
        {'literal': ['boolLiteral']},
        {'stringLiteral': ['stringLiteral']},
        {'charLiteral': ['charLiteral']},
        {'boolLiteral': ['boolLiteral']},
        {'intLiteral': ['intLiteral']}, 
        {'id': ['id']} ]

    dfa = {
            0:{'{':['shift',1]},
            1:{'}':['reduce',2],'{':['shift',1],'type':['shift',17],'if':['shift',8],'for':['shift',9],'return':['shift',10],'break':['shift',11],'continue':['shift',12],'callout':['shift',16],'id':['shift',15],'statementList':['goTo',2],'statement':['goTo',4],'location':['goTo',5],'methodCall':['goTo',6],'block':['goTo',13],'varDecl':['goTo',14],'methodName':['goTo',24]},
            2:{'}':['shift',3]},
            3:{'{':['reduce',1],'}':['reduce',1],',':['reduce',1],'[':['reduce',1],']':['reduce',1],';':['reduce',1],'type':['reduce',1],'void':['reduce',1],'if':['reduce',1],'(':['reduce',1],')':['reduce',1],'else':['reduce',1],'for':['reduce',1],'return':['reduce',1],'break':['reduce',1],'continue':['reduce',1],'assignOperators':['reduce',1],'callout':['reduce',1],'operadores':['reduce',1],'equalityOperatos':['reduce',1],'conditionOperators':['reduce',1],'boolLiteral':['reduce',1],'charLiteral':['reduce',1],'stringLiteral':['reduce',1],'intLiteral':['reduce',1],'id':['reduce',1],'menos':['reduce',1],'!':['reduce',1],'menos':['reduce',1],'!':['reduce',1],'statementList':['reduce',1],'statement':['reduce',1],'location':['reduce',1],'methodCall':['reduce',1],'block':['reduce',1],'varDecl':['reduce',1],'expr':['reduce',1],'methodName':['reduce',1],'literal':['reduce',1],'-':['reduce',1],'!':['reduce',1],'=':['reduce',1],'listExp':['reduce',1],'binOp':['reduce',1],'calloutArgsL':['reduce',1],'argCallout':['reduce',1]},
            4:{'{':['shift',0],'}':['reduce',2],',':['reduce',2],'[':['reduce',2],']':['reduce',2],';':['reduce',2],'type':['shift',17],'void':['reduce',2],'if':['shift',8],'(':['reduce',2],')':['reduce',2],'else':['reduce',2],'for':['shift',9],'return':['shift',10],'break':['shift',11],'continue':['shift',12],'assignOperators':['reduce',2],'callout':['shift',16],'operadores':['reduce',2],'equalityOperators':['reduce',2],'conditionOperators':['reduce',2],'boolLiteral':['reduce',2],'charLiteral':['reduce',2],'stringLiteral':['reduce',2],'intLiteral':['reduce',2],'id':['shift',15],'menos':['reduce',2],'!':['reduce',2],'menos':['reduce',2],'!':['reduce',2],'statementList':['goTo',18],'statement':['goTo',4],'location':['goTo',5],'methodCall':['goTo',6],'block':['goTo',13],'varDecl':['goTo',14],'expr':['reduce',2],'methodName':['goTo',24],'literal':['reduce',2],'-':['reduce',2],'!':['reduce',2],'=':['reduce',2],'listExp':['reduce',2],'binOp':['reduce',2],'calloutArgsL':['reduce',2],'argCallout':['reduce',2]},
            5:{'statement':['goTo',4],'}':['reduce',2],'assignOperators':['shift',19]},
            6:{';':['shift',7],'(':['shift',25]},
            7:{'{':['reduce',6],'}':['reduce',6],',':['reduce',6],'[':['reduce',6],']':['reduce',6],';':['reduce',6],'type':['reduce',6],'void':['reduce',6],'if':['reduce',6],'(':['reduce',6],')':['reduce',6],'else':['reduce',6],'for':['reduce',6],'return':['reduce',6],'break':['reduce',6],'continue':['reduce',6],'assignOperators':['reduce',6],'callout':['reduce',6],'operadores':['reduce',6],'equalityOperators':['reduce',6],'conditionOperators':['reduce',6],'boolLiteral':['reduce',6],'charLiteral':['reduce',6],'stringLiteral':['reduce',6],'intLiteral':['reduce',6],'id':['reduce',6],'menos':['reduce',6],'!':['reduce',6],'menos':['reduce',6],'!':['reduce',6],'statementList':['reduce',6],'statement':['reduce',6],'location':['reduce',6],'methodCall':['reduce',6],'block':['reduce',6],'varDecl':['reduce',6],'expr':['reduce',6],'methodName':['reduce',6],'literal':['reduce',6],'-':['reduce',6],'!':['reduce',6],'=':['reduce',6],'listExp':['reduce',6],'binOp':['reduce',6],'calloutArgsL':['reduce',6],'argCallout':['reduce',6]},
            8:{'(':['shift',20]},
            9:{'id':['shift',21]},
            10:{';':['shift',22],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            11:{';':['shift',36]},
            12:{';':['shift',37]},
            13:{'{':['reduce',14],'}':['reduce',14],',':['reduce',14],'[':['reduce',14],']':['reduce',14],';':['reduce',14],'type':['reduce',14],'void':['reduce',14],'if':['reduce',14],'(':['reduce',14],')':['reduce',14],'else':['reduce',14],'for':['reduce',14],'return':['reduce',14],'break':['reduce',14],'continue':['reduce',14],'assignOperators':['reduce',14],'callout':['reduce',14],'operadores':['reduce',14],'equalityOperators':['reduce',14],'conditionOperators':['reduce',14],'boolLiteral':['reduce',14],'charLiteral':['reduce',14],'stringLiteral':['reduce',14],'intLiteral':['reduce',14],'id':['reduce',14],'menos':['reduce',14],'!':['reduce',14],'menos':['reduce',14],'!':['reduce',14],'statementList':['reduce',14],'statement':['reduce',14],'location':['reduce',14],'methodCall':['reduce',14],'block':['reduce',14],'varDecl':['reduce',14],'expr':['reduce',14],'methodName':['reduce',14],'literal':['reduce',14],'-':['reduce',14],'!':['reduce',14],'=':['reduce',14],'listExp':['reduce',14],'binOp':['reduce',14],'calloutArgsL':['reduce',14],'argCallout':['reduce',14]},
            14:{'{':['reduce',15],'}':['reduce',15],',':['reduce',15],'[':['reduce',15],']':['reduce',15],';':['reduce',15],'type':['reduce',15],'void':['reduce',15],'if':['reduce',15],'(':['reduce',15],')':['reduce',15],'else':['reduce',15],'for':['reduce',15],'return':['reduce',15],'break':['reduce',15],'continue':['reduce',15],'assignOperators':['reduce',15],'callout':['reduce',15],'operadores':['reduce',15],'equalityOperators':['reduce',15],'conditionOperators':['reduce',15],'boolLiteral':['reduce',15],'charLiteral':['reduce',15],'stringLiteral':['reduce',15],'intLiteral':['reduce',15],'id':['reduce',15],'menos':['reduce',15],'!':['reduce',15],'menos':['reduce',15],'!':['reduce',15],'statementList':['reduce',15],'statement':['reduce',15],'location':['reduce',15],'methodCall':['reduce',15],'block':['reduce',15],'varDecl':['reduce',15],'expr':['reduce',15],'methodName':['reduce',15],'literal':['reduce',15],'-':['reduce',15],'!':['reduce',15],'=':['reduce',15],'listExp':['reduce',15],'binOp':['reduce',15],'calloutArgsL':['reduce',15],'argCallout':['reduce',15]},
            15:{'{':['reduce',23],'}':['reduce',23],',':['reduce',23],'[':['shift',38],']':['reduce',23],';':['reduce',23],'type':['reduce',23],'void':['reduce',23],'if':['reduce',23],'(':['reduce',25],')':['reduce',23],'else':['reduce',23],'for':['reduce',23],'return':['reduce',23],'break':['reduce',23],'continue':['reduce',23],'assignOperators':['reduce',23],'callout':['reduce',23],'operadores':['reduce',23],'equalityOperators':['reduce',23],'conditionOperators':['reduce',23],'boolLiteral':['reduce',23],'charLiteral':['reduce',23],'stringLiteral':['reduce',23],'intLiteral':['reduce',23],'id':['reduce',23],'menos':['reduce',23],'!':['reduce',23],'menos':['reduce',23],'!':['reduce',23],'statementList':['reduce',23],'statement':['reduce',23],'location':['reduce',23],'methodCall':['reduce',23],'block':['reduce',23],'varDecl':['reduce',23],'expr':['reduce',23],'methodName':['reduce',23],'literal':['reduce',23],'-':['reduce',23],'!':['reduce',23],'=':['reduce',23],'listExp':['reduce',23],'binOp':['reduce',23],'calloutArgsL':['reduce',23],'argCallout':['reduce',23]},
            16:{'(':['shift',39]},
            17:{'id':['shift',40]},
            18:{'{':['reduce',3],'}':['reduce',3],',':['reduce',3],'[':['reduce',3],']':['reduce',3],';':['reduce',3],'type':['reduce',3],'void':['reduce',3],'if':['reduce',3],'(':['reduce',3],')':['reduce',3],'else':['reduce',3],'for':['reduce',3],'return':['reduce',3],'break':['reduce',3],'continue':['reduce',3],'assignOperators':['reduce',3],'callout':['reduce',3],'operadores':['reduce',3],'equalityOperators':['reduce',3],'conditionOperators':['reduce',3],'boolLiteral':['reduce',3],'charLiteral':['reduce',3],'stringLiteral':['reduce',3],'intLiteral':['reduce',3],'id':['reduce',3],'menos':['reduce',3],'!':['reduce',3],'menos':['reduce',3],'!':['reduce',3],'statementList':['reduce',3],'statement':['reduce',3],'location':['reduce',3],'methodCall':['reduce',3],'block':['reduce',3],'varDecl':['reduce',3],'expr':['reduce',3],'methodName':['reduce',3],'literal':['reduce',3],'-':['reduce',3],'!':['reduce',3],'=':['reduce',3],'listExp':['reduce',3],'binOp':['reduce',3],'calloutArgsL':['reduce',3],'argCallout':['reduce',3]},
            19:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'menos':['goTo',33]},
            20:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33],'=':['goTo',45]},
            21:{'assignOperators':['shift',45]},
            22:{'{':['reduce',10],'}':['reduce',10],',':['reduce',10],'[':['reduce',10],']':['reduce',10],';':['reduce',10],'type':['reduce',10],'void':['reduce',10],'if':['reduce',10],'(':['reduce',10],')':['reduce',10],'else':['reduce',10],'for':['reduce',10],'return':['reduce',10],'break':['reduce',10],'continue':['reduce',10],'assignOperators':['reduce',10],'callout':['reduce',10],'operadores':['reduce',10],'equalityOperators':['reduce',10],'conditionOperators':['reduce',10],'boolLiteral':['reduce',10],'charLiteral':['reduce',10],'stringLiteral':['reduce',10],'intLiteral':['reduce',10],'id':['reduce',10],'menos':['reduce',10],'!':['reduce',10],'menos':['reduce',10],'!':['reduce',10],'statementList':['reduce',10],'statement':['reduce',10],'location':['reduce',10],'methodCall':['reduce',10],'block':['reduce',10],'varDecl':['reduce',10],'expr':['reduce',10],'methodName':['reduce',10],'literal':['reduce',10],'-':['reduce',10],'!':['reduce',10],'=':['reduce',10],'listExp':['reduce',10],'binOp':['reduce',10],'calloutArgsL':['reduce',10],'argCallout':['reduce',10]},
            23:{';':['shift',86]},
            24:{'(':['shift',46]},
            25:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',50],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33],'listExp':['goTo',48]},
            26:{'{':['reduce',16],'}':['reduce',16],',':['reduce',16],'[':['reduce',16],']':['reduce',16],';':['reduce',16],'type':['reduce',16],'void':['reduce',16],'if':['reduce',16],'(':['reduce',16],')':['reduce',16],'else':['reduce',16],'for':['reduce',16],'return':['reduce',16],'break':['reduce',16],'continue':['reduce',16],'assignOperators':['reduce',16],'callout':['reduce',16],'operadores':['reduce',16],'equalityOperators':['reduce',16],'conditionOperators':['reduce',16],'boolLiteral':['reduce',16],'charLiteral':['reduce',16],'stringLiteral':['reduce',16],'intLiteral':['reduce',16],'id':['reduce',16],'menos':['reduce',16],'!':['reduce',16],'menos':['reduce',16],'!':['reduce',16],'statementList':['reduce',16],'statement':['reduce',16],'location':['reduce',16],'methodCall':['reduce',16],'block':['reduce',16],'varDecl':['reduce',16],'expr':['reduce',16],'methodName':['reduce',16],'literal':['reduce',16],'-':['reduce',16],'!':['reduce',16],'=':['reduce',16],'listExp':['reduce',16],'binOp':['reduce',16],'calloutArgsL':['reduce',16],'argCallout':['reduce',16]},
            27:{'{':['reduce',17],'}':['reduce',17],',':['reduce',17],'[':['reduce',17],']':['reduce',17],';':['reduce',17],'type':['reduce',17],'void':['reduce',17],'if':['reduce',17],'(':['shift',51],')':['reduce',17],'else':['reduce',17],'for':['reduce',17],'return':['reduce',17],'break':['reduce',17],'continue':['reduce',17],'assignOperators':['reduce',17],'callout':['reduce',17],'operadores':['reduce',17],'equalityOperators':['reduce',17],'conditionOperators':['reduce',17],'boolLiteral':['reduce',17],'charLiteral':['reduce',17],'stringLiteral':['reduce',17],'intLiteral':['reduce',17],'id':['reduce',17],'menos':['reduce',17],'!':['reduce',17],'menos':['reduce',17],'!':['reduce',17],'statementList':['reduce',17],'statement':['reduce',17],'location':['reduce',17],'methodCall':['goTo',27],'block':['reduce',17],'varDecl':['reduce',17],'expr':['reduce',17],'methodName':['reduce',17],'literal':['reduce',17],'-':['reduce',17],'!':['reduce',17],'=':['reduce',17],'listExp':['reduce',17],'binOp':['reduce',17],'calloutArgsL':['reduce',17],'argCallout':['reduce',17]},
            28:{'{':['reduce',18],'}':['reduce',18],',':['reduce',18],'[':['reduce',18],']':['reduce',18],';':['reduce',18],'type':['reduce',18],'void':['reduce',18],'if':['reduce',18],'(':['reduce',18],')':['reduce',18],'else':['reduce',18],'for':['reduce',18],'return':['reduce',18],'break':['reduce',18],'continue':['reduce',18],'assignOperators':['reduce',18],'callout':['reduce',18],'operadores':['reduce',18],'equalityOperators':['reduce',18],'conditionOperators':['reduce',18],'boolLiteral':['reduce',18],'charLiteral':['reduce',18],'stringLiteral':['reduce',18],'intLiteral':['reduce',18],'id':['reduce',18],'menos':['reduce',18],'!':['reduce',18],'menos':['reduce',18],'!':['reduce',18],'statementList':['reduce',18],'statement':['reduce',18],'location':['reduce',18],'methodCall':['reduce',18],'block':['reduce',18],'varDecl':['reduce',18],'expr':['reduce',18],'methodName':['reduce',18],'literal':['reduce',18],'-':['reduce',18],'!':['reduce',18],'=':['reduce',18],'listExp':['reduce',18],'binOp':['reduce',18],'calloutArgsL':['reduce',18],'argCallout':['reduce',18]},
            29:{'{':['reduce',44],'}':['reduce',44],',':['reduce',44],'[':['reduce',44],']':['reduce',44],';':['reduce',44],'type':['reduce',44],'void':['reduce',44],'if':['reduce',44],'(':['reduce',44],')':['reduce',44],'else':['reduce',44],'for':['reduce',44],'return':['reduce',44],'break':['reduce',44],'continue':['reduce',44],'assignOperators':['reduce',44],'callout':['reduce',44],'operadores':['reduce',44],'equalityOperators':['reduce',44],'conditionOperators':['reduce',44],'boolLiteral':['reduce',44],'charLiteral':['reduce',44],'stringLiteral':['reduce',44],'intLiteral':['reduce',44],'id':['reduce',44],'menos':['reduce',44],'!':['reduce',44],'menos':['reduce',44],'!':['reduce',44],'statementList':['reduce',44],'statement':['reduce',44],'location':['reduce',44],'methodCall':['reduce',44],'block':['reduce',44],'varDecl':['reduce',44],'expr':['reduce',44],'methodName':['reduce',44],'literal':['reduce',44],'-':['reduce',44],'!':['reduce',44],'=':['reduce',44],'listExp':['reduce',44],'binOp':['reduce',44],'calloutArgsL':['reduce',44],'argCallout':['reduce',44]},
            30:{'{':['reduce',45],'}':['reduce',45],',':['reduce',45],'[':['reduce',45],']':['reduce',45],';':['reduce',45],'type':['reduce',45],'void':['reduce',45],'if':['reduce',45],'(':['reduce',45],')':['reduce',45],'else':['reduce',45],'for':['reduce',45],'return':['reduce',45],'break':['reduce',45],'continue':['reduce',45],'assignOperators':['reduce',45],'callout':['reduce',45],'operadores':['reduce',45],'equalityOperators':['reduce',45],'conditionOperators':['reduce',45],'boolLiteral':['reduce',45],'charLiteral':['reduce',45],'stringLiteral':['reduce',45],'intLiteral':['reduce',45],'id':['reduce',45],'menos':['reduce',45],'!':['reduce',45],'menos':['reduce',45],'!':['reduce',45],'statementList':['reduce',45],'statement':['reduce',45],'location':['reduce',45],'methodCall':['reduce',45],'block':['reduce',45],'varDecl':['reduce',45],'expr':['reduce',45],'methodName':['reduce',45],'literal':['reduce',45],'-':['reduce',45],'!':['reduce',45],'=':['reduce',45],'listExp':['reduce',45],'binOp':['reduce',45],'calloutArgsL':['reduce',45],'argCallout':['reduce',45]},
            31:{'{':['reduce',46],'}':['reduce',46],',':['reduce',46],'[':['reduce',46],']':['reduce',46],';':['reduce',46],'type':['reduce',46],'void':['reduce',46],'if':['reduce',46],'(':['reduce',46],')':['reduce',46],'else':['reduce',46],'for':['reduce',46],'return':['reduce',46],'break':['reduce',46],'continue':['reduce',46],'assignOperators':['reduce',46],'callout':['reduce',46],'operadores':['reduce',46],'equalityOperators':['reduce',46],'conditionOperators':['reduce',46],'boolLiteral':['reduce',46],'charLiteral':['reduce',46],'stringLiteral':['reduce',46],'intLiteral':['reduce',46],'id':['reduce',46],'menos':['reduce',46],'!':['reduce',46],'menos':['reduce',46],'!':['reduce',46],'statementList':['reduce',46],'statement':['reduce',46],'location':['reduce',46],'methodCall':['reduce',46],'block':['reduce',46],'varDecl':['reduce',46],'expr':['reduce',46],'methodName':['reduce',46],'literal':['reduce',46],'-':['reduce',46],'!':['reduce',46],'=':['reduce',46],'listExp':['reduce',46],'binOp':['reduce',46],'calloutArgsL':['reduce',46],'argCallout':['reduce',46]},
            32:{';':['shift', 43],')':['reduce',19],'operadores':['shift',53],'equalityOperators':['shift',55],'conditionOperators':['shift',56],'binOp':['goTo',52],'menos':['shift',52]},
            33:{'!':['shift',34],'menos':['shift',33],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            34:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            35:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            36:{'{':['reduce',12],'}':['reduce',12],',':['reduce',12],'[':['reduce',12],']':['reduce',12],';':['reduce',12],'type':['reduce',12],'void':['reduce',12],'if':['reduce',12],'(':['reduce',12],')':['reduce',12],'else':['reduce',12],'for':['reduce',12],'return':['reduce',12],'break':['reduce',12],'continue':['reduce',12],'assignOperators':['reduce',12],'callout':['reduce',12],'operadores':['reduce',12],'equalityOperators':['reduce',12],'conditionOperators':['reduce',12],'boolLiteral':['reduce',12],'charLiteral':['reduce',12],'stringLiteral':['reduce',12],'intLiteral':['reduce',12],'id':['reduce',12],'menos':['reduce',12],'!':['reduce',12],'menos':['reduce',12],'!':['reduce',12],'statementList':['reduce',12],'statement':['reduce',12],'location':['reduce',12],'methodCall':['reduce',12],'block':['reduce',12],'varDecl':['reduce',12],'expr':['reduce',12],'methodName':['reduce',12],'literal':['reduce',12],'-':['reduce',12],'!':['reduce',12],'=':['reduce',12],'listExp':['reduce',12],'binOp':['reduce',12],'calloutArgsL':['reduce',12],'argCallout':['reduce',12]},
            37:{'{':['reduce',13],'}':['reduce',13],',':['reduce',13],'[':['reduce',13],']':['reduce',13],';':['reduce',13],'type':['reduce',13],'void':['reduce',13],'if':['reduce',13],'(':['reduce',13],')':['reduce',13],'else':['reduce',13],'for':['reduce',13],'return':['reduce',13],'break':['reduce',13],'continue':['reduce',13],'assignOperators':['reduce',13],'callout':['reduce',13],'operadores':['reduce',13],'equalityOperators':['reduce',13],'conditionOperators':['reduce',13],'boolLiteral':['reduce',13],'charLiteral':['reduce',13],'stringLiteral':['reduce',13],'intLiteral':['reduce',13],'id':['reduce',13],'menos':['reduce',13],'!':['reduce',13],'menos':['reduce',13],'!':['reduce',13],'statementList':['reduce',13],'statement':['reduce',13],'location':['reduce',13],'methodCall':['reduce',13],'block':['reduce',13],'varDecl':['reduce',13],'expr':['reduce',13],'methodName':['reduce',13],'literal':['reduce',13],'-':['reduce',13],'!':['reduce',13],'=':['reduce',13],'listExp':['reduce',13],'binOp':['reduce',13],'calloutArgsL':['reduce',13],'argCallout':['reduce',13]},
            38:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            39:{'stringLiteral':['shift',63]},
            40:{';':['shift',41]},
            41:{'{':['reduce',4],'}':['reduce',4],',':['reduce',4],'[':['reduce',4],']':['reduce',4],';':['reduce',4],'type':['reduce',4],'void':['reduce',4],'if':['reduce',4],'(':['reduce',4],')':['reduce',4],'else':['reduce',4],'for':['reduce',4],'return':['reduce',4],'break':['reduce',4],'continue':['reduce',4],'assignOperators':['reduce',4],'callout':['reduce',4],'operadores':['reduce',4],'equalityOperators':['reduce',4],'conditionOperators':['reduce',4],'boolLiteral':['reduce',4],'charLiteral':['reduce',4],'stringLiteral':['reduce',4],'intLiteral':['reduce',4],'id':['reduce',4],'menos':['reduce',4],'!':['reduce',4],'menos':['reduce',4],'!':['reduce',4],'statementList':['reduce',4],'statement':['reduce',4],'location':['reduce',4],'methodCall':['reduce',4],'block':['reduce',4],'varDecl':['reduce',4],'expr':['reduce',4],'methodName':['reduce',4],'literal':['reduce',4],'-':['reduce',4],'!':['reduce',4],'=':['reduce',4],'listExp':['reduce',4],'binOp':['reduce',4],'calloutArgsL':['reduce',4],'argCallout':['reduce',4]},
            42:{';':['shift',43]},
            43:{'{':['reduce',5],'}':['reduce',5],',':['reduce',5],'[':['reduce',5],']':['reduce',5],';':['reduce',5],'type':['reduce',5],'void':['reduce',5],'if':['reduce',5],'(':['reduce',5],')':['reduce',5],'else':['reduce',5],'for':['reduce',5],'return':['reduce',5],'break':['reduce',5],'continue':['reduce',5],'assignOperators':['reduce',5],'callout':['reduce',5],'operadores':['reduce',5],'equalityOperators':['reduce',5],'conditionOperators':['reduce',5],'boolLiteral':['reduce',5],'charLiteral':['reduce',5],'stringLiteral':['reduce',5],'intLiteral':['reduce',5],'id':['reduce',5],'menos':['reduce',5],'!':['reduce',5],'menos':['reduce',5],'!':['reduce',5],'statementList':['reduce',5],'statement':['reduce',5],'location':['reduce',5],'methodCall':['reduce',5],'block':['reduce',5],'varDecl':['reduce',5],'expr':['reduce',5],'methodName':['reduce',5],'literal':['reduce',5],'-':['reduce',5],'!':['reduce',5],'=':['reduce',5],'listExp':['reduce',5],'binOp':['reduce',5],'calloutArgsL':['reduce',5],'argCallout':['reduce',5]},
            44:{')':['shift',64]},
            45:{'!':['shift',34],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33],},
            46:{')':['shift',47]},
            47:{'{':['reduce',26],'}':['reduce',26],',':['reduce',26],'[':['reduce',26],']':['reduce',26],';':['reduce',26],'type':['reduce',26],'void':['reduce',26],'if':['reduce',26],'(':['reduce',26],')':['reduce',26],'else':['reduce',26],'for':['reduce',26],'return':['reduce',26],'break':['reduce',26],'continue':['reduce',26],'assignOperators':['reduce',26],'callout':['reduce',26],'operadores':['reduce',26],'equalityOperators':['reduce',26],'conditionOperators':['reduce',26],'boolLiteral':['reduce',26],'charLiteral':['reduce',26],'stringLiteral':['reduce',26],'intLiteral':['reduce',26],'id':['reduce',26],'menos':['reduce',26],'!':['reduce',26],'menos':['reduce',26],'!':['reduce',26],'statementList':['reduce',26],'statement':['reduce',26],'location':['reduce',26],'methodCall':['reduce',26],'block':['reduce',26],'varDecl':['reduce',26],'expr':['reduce',26],'methodName':['reduce',26],'literal':['reduce',26],'-':['reduce',26],'!':['reduce',26],'=':['reduce',26],'listExp':['reduce',26],'binOp':['reduce',26],'calloutArgsL':['reduce',26],'argCallout':['reduce',26]},
            48:{')':['shift',49]},
            49:{'{':['reduce',27],'}':['reduce',27],',':['reduce',27],'[':['reduce',27],']':['reduce',27],';':['reduce',27],'type':['reduce',27],'void':['reduce',27],'if':['reduce',27],'(':['reduce',27],')':['reduce',27],'else':['reduce',27],'for':['reduce',27],'return':['reduce',27],'break':['reduce',27],'continue':['reduce',27],'assignOperators':['reduce',27],'callout':['reduce',27],'operadores':['reduce',27],'equalityOperators':['reduce',27],'conditionOperators':['reduce',27],'boolLiteral':['reduce',27],'charLiteral':['reduce',27],'stringLiteral':['reduce',27],'intLiteral':['reduce',27],'id':['reduce',27],'menos':['reduce',27],'!':['reduce',27],'menos':['reduce',27],'!':['reduce',27],'statementList':['reduce',27],'statement':['reduce',27],'location':['reduce',27],'methodCall':['reduce',27],'block':['reduce',27],'varDecl':['reduce',27],'expr':['reduce',27],'methodName':['reduce',27],'literal':['reduce',27],'-':['reduce',27],'!':['reduce',27],'=':['reduce',27],'listExp':['reduce',27],'binOp':['reduce',27],'calloutArgsL':['reduce',27],'argCallout':['reduce',27]},
            50:{'{':['reduce',32],'}':['reduce',32],',':['shift',66],'[':['reduce',32],']':['reduce',32],';':['reduce',32],'type':['reduce',32],'void':['reduce',32],'if':['reduce',32],'(':['reduce',32],')':['reduce',32],'else':['reduce',32],'for':['reduce',32],'return':['reduce',32],'break':['reduce',32],'continue':['reduce',32],'assignOperators':['reduce',32],'callout':['reduce',32],'operadores':['reduce',32],'equalityOperators':['reduce',32],'conditionOperators':['reduce',32],'boolLiteral':['reduce',32],'charLiteral':['reduce',32],'stringLiteral':['reduce',32],'intLiteral':['reduce',32],'id':['reduce',32],'menos':['reduce',32],'!':['reduce',32],'menos':['reduce',32],'!':['reduce',32],'statementList':['reduce',32],'statement':['reduce',32],'location':['reduce',32],'methodCall':['reduce',32],'block':['reduce',32],'varDecl':['reduce',32],'expr':['goTo',66],'methodName':['reduce',32],'literal':['reduce',32],'-':['reduce',32],'!':['reduce',32],'=':['reduce',32],'listExp':['reduce',32],'binOp':['reduce',32],'calloutArgsL':['reduce',32],'argCallout':['reduce',32]},
            51:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',28],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33],'listExp':['shift',67]},
            52:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',51],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            53:{'{':['reduce',36],'}':['reduce',36],',':['reduce',36],'[':['reduce',36],']':['reduce',36],';':['reduce',36],'type':['reduce',36],'void':['reduce',36],'if':['reduce',36],'(':['reduce',36],')':['reduce',36],'else':['reduce',36],'for':['reduce',36],'return':['reduce',36],'break':['reduce',36],'continue':['reduce',36],'assignOperators':['reduce',36],'callout':['reduce',36],'operadores':['reduce',36],'equalityOperators':['reduce',36],'conditionOperators':['reduce',36],'boolLiteral':['reduce',36],'charLiteral':['reduce',36],'stringLiteral':['reduce',36],'intLiteral':['reduce',36],'id':['reduce',36],'menos':['reduce',36],'!':['reduce',36],'menos':['reduce',36],'!':['reduce',36],'statementList':['reduce',36],'statement':['reduce',36],'location':['reduce',36],'methodCall':['reduce',36],'block':['reduce',36],'varDecl':['reduce',36],'expr':['reduce',36],'methodName':['reduce',36],'literal':['reduce',36],'-':['reduce',36],'!':['reduce',36],'=':['reduce',36],'listExp':['reduce',36],'binOp':['reduce',36],'calloutArgsL':['reduce',36],'argCallout':['reduce',36]},
            54:{'{':['reduce',37],'}':['reduce',37],',':['reduce',37],'[':['reduce',37],']':['reduce',37],';':['reduce',37],'type':['reduce',37],'void':['reduce',37],'if':['reduce',37],'(':['reduce',37],')':['reduce',37],'else':['reduce',37],'for':['reduce',37],'return':['reduce',37],'break':['reduce',37],'continue':['reduce',37],'assignOperators':['reduce',37],'callout':['reduce',37],'operadores':['reduce',37],'equalityOperators':['reduce',37],'conditionOperators':['reduce',37],'boolLiteral':['reduce',37],'charLiteral':['reduce',37],'stringLiteral':['reduce',37],'intLiteral':['reduce',37],'id':['reduce',37],'menos':['reduce',37],'!':['reduce',37],'menos':['reduce',37],'!':['reduce',37],'statementList':['reduce',37],'statement':['reduce',37],'location':['reduce',37],'methodCall':['reduce',37],'block':['reduce',37],'varDecl':['reduce',37],'expr':['reduce',37],'methodName':['reduce',37],'literal':['reduce',37],'-':['reduce',37],'!':['reduce',37],'=':['reduce',37],'listExp':['reduce',37],'binOp':['reduce',37],'calloutArgsL':['reduce',37],'argCallout':['reduce',37]},
            55:{'{':['reduce',38],'}':['reduce',38],',':['reduce',38],'[':['reduce',38],']':['reduce',38],';':['reduce',38],'type':['reduce',38],'void':['reduce',38],'if':['reduce',38],'(':['reduce',38],')':['reduce',38],'else':['reduce',38],'for':['reduce',38],'return':['reduce',38],'break':['reduce',38],'continue':['reduce',38],'assignOperators':['reduce',38],'callout':['reduce',38],'operadores':['reduce',38],'equalityOperators':['reduce',38],'conditionOperators':['reduce',38],'boolLiteral':['reduce',38],'charLiteral':['reduce',38],'stringLiteral':['reduce',38],'intLiteral':['reduce',38],'id':['reduce',38],'menos':['reduce',38],'!':['reduce',38],'menos':['reduce',38],'!':['reduce',38],'statementList':['reduce',38],'statement':['reduce',38],'location':['reduce',38],'methodCall':['reduce',38],'block':['reduce',38],'varDecl':['reduce',38],'expr':['reduce',38],'methodName':['reduce',38],'literal':['reduce',38],'-':['reduce',38],'!':['reduce',38],'=':['reduce',38],'listExp':['reduce',38],'binOp':['reduce',38],'calloutArgsL':['reduce',38],'argCallout':['reduce',38]},
            56:{'{':['reduce',39],'}':['reduce',39],',':['reduce',39],'[':['reduce',39],']':['reduce',39],';':['reduce',39],'type':['reduce',39],'void':['reduce',39],'if':['reduce',39],'(':['reduce',39],')':['reduce',39],'else':['reduce',39],'for':['reduce',39],'return':['reduce',39],'break':['reduce',39],'continue':['reduce',39],'assignOperators':['reduce',39],'callout':['reduce',39],'operadores':['reduce',39],'equalityOperators':['reduce',39],'conditionOperators':['reduce',39],'boolLiteral':['reduce',39],'charLiteral':['reduce',39],'stringLiteral':['reduce',39],'intLiteral':['reduce',39],'id':['reduce',39],'menos':['reduce',39],'!':['reduce',39],'menos':['reduce',39],'!':['reduce',39],'statementList':['reduce',39],'statement':['reduce',39],'location':['reduce',39],'methodCall':['reduce',39],'block':['reduce',39],'varDecl':['reduce',39],'expr':['reduce',39],'methodName':['reduce',39],'literal':['reduce',39],'-':['reduce',39],'!':['reduce',39],'=':['reduce',39],'listExp':['reduce',39],'binOp':['reduce',39],'calloutArgsL':['reduce',39],'argCallout':['reduce',39]},
            57:{'{':['reduce',20],'}':['reduce',20],',':['reduce',20],'[':['reduce',20],']':['reduce',20],';':['reduce',20],'type':['reduce',20],'void':['reduce',20],'if':['reduce',20],'(':['reduce',20],')':['reduce',20],'else':['reduce',20],'for':['reduce',20],'return':['reduce',20],'break':['reduce',20],'continue':['reduce',20],'assignOperators':['reduce',20],'callout':['reduce',20],'operadores':['reduce',20],'equalityOperators':['reduce',20],'conditionOperators':['reduce',20],'boolLiteral':['reduce',20],'charLiteral':['reduce',20],'stringLiteral':['reduce',20],'intLiteral':['reduce',20],'id':['reduce',20],'menos':['reduce',20],'!':['reduce',20],'menos':['reduce',20],'!':['reduce',20],'statementList':['reduce',20],'statement':['reduce',20],'location':['reduce',20],'methodCall':['reduce',20],'block':['reduce',20],'varDecl':['reduce',20],'expr':['reduce',20],'methodName':['reduce',20],'literal':['reduce',20],'-':['reduce',20],'!':['reduce',20],'=':['reduce',20],'listExp':['reduce',20],'binOp':['reduce',20],'calloutArgsL':['reduce',20],'argCallout':['reduce',20]},
            58:{'{':['reduce',21],'}':['reduce',21],',':['reduce',21],'[':['reduce',21],']':['reduce',21],';':['reduce',21],'type':['reduce',21],'void':['reduce',21],'if':['reduce',21],'(':['reduce',21],')':['reduce',21],'else':['reduce',21],'for':['reduce',21],'return':['reduce',21],'break':['reduce',21],'continue':['reduce',21],'assignOperators':['reduce',21],'callout':['reduce',21],'operadores':['reduce',21],'equalityOperators':['reduce',21],'conditionOperators':['reduce',21],'boolLiteral':['reduce',21],'charLiteral':['reduce',21],'stringLiteral':['reduce',21],'intLiteral':['reduce',21],'id':['reduce',21],'menos':['reduce',21],'!':['reduce',21],'menos':['reduce',21],'!':['reduce',21],'statementList':['reduce',21],'statement':['reduce',21],'location':['reduce',21],'methodCall':['reduce',21],'block':['reduce',21],'varDecl':['reduce',21],'expr':['reduce',21],'methodName':['reduce',21],'literal':['reduce',21],'-':['reduce',21],'!':['reduce',21],'=':['reduce',21],'listExp':['reduce',21],'binOp':['reduce',21],'calloutArgsL':['reduce',21],'argCallout':['reduce',21]},
            59:{')':['shift',60]},
            60:{'{':['reduce',22],'}':['reduce',22],',':['reduce',22],'[':['reduce',22],']':['reduce',22],';':['reduce',22],'type':['reduce',22],'void':['reduce',22],'if':['reduce',22],'(':['reduce',22],')':['reduce',22],'else':['reduce',22],'for':['reduce',22],'return':['reduce',22],'break':['reduce',22],'continue':['reduce',22],'assignOperators':['reduce',22],'callout':['reduce',22],'operadores':['reduce',22],'equalityOperators':['reduce',22],'conditionOperators':['reduce',22],'boolLiteral':['reduce',22],'charLiteral':['reduce',22],'stringLiteral':['reduce',22],'intLiteral':['reduce',22],'id':['reduce',22],'menos':['reduce',22],'!':['reduce',22],'menos':['reduce',22],'!':['reduce',22],'statementList':['reduce',22],'statement':['reduce',22],'location':['reduce',22],'methodCall':['reduce',22],'block':['reduce',22],'varDecl':['reduce',22],'expr':['reduce',22],'methodName':['reduce',22],'literal':['reduce',22],'-':['reduce',22],'!':['reduce',22],'=':['reduce',22],'listExp':['reduce',22],'binOp':['reduce',22],'calloutArgsL':['reduce',22],'argCallout':['reduce',22]},
            61:{',':['shift',70],']':['shift',62],')':['shift',70]},
            62:{'{':['reduce',24],'}':['reduce',24],',':['reduce',24],'[':['reduce',24],']':['reduce',24],';':['reduce',24],'type':['reduce',24],'void':['reduce',24],'if':['reduce',24],'(':['reduce',24],')':['reduce',24],'else':['reduce',24],'for':['reduce',24],'return':['reduce',24],'break':['reduce',24],'continue':['reduce',24],'assignOperators':['reduce',24],'callout':['reduce',24],'operadores':['reduce',24],'equalityOperators':['reduce',24],'conditionOperators':['reduce',24],'boolLiteral':['reduce',24],'charLiteral':['reduce',24],'stringLiteral':['reduce',24],'intLiteral':['reduce',24],'id':['reduce',24],'menos':['reduce',24],'!':['reduce',24],'menos':['reduce',24],'!':['reduce',24],'statementList':['reduce',24],'statement':['reduce',24],'location':['reduce',24],'methodCall':['reduce',24],'block':['reduce',24],'varDecl':['reduce',24],'expr':['reduce',24],'methodName':['reduce',24],'literal':['reduce',24],'-':['reduce',24],'!':['reduce',24],'=':['reduce',24],'listExp':['reduce',24],'binOp':['reduce',24],'calloutArgsL':['reduce',24],'argCallout':['reduce',24]},
            63:{',':['shift',71],')':['shift',71],'stringLiteral':['shift',63]},
            64:{'{':['shift',1],'block':['goTo',72]},
            65:{',':['shift',73]},
            66:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33],'listExp':['goTo',74]},
            67:{')':['shift',68]},
            68:{'{':['reduce',27],'}':['reduce',27],',':['reduce',27],'[':['reduce',27],']':['reduce',27],';':['reduce',27],'type':['reduce',27],'void':['reduce',27],'if':['reduce',27],'(':['reduce',27],')':['reduce',27],'else':['reduce',27],'for':['reduce',27],'return':['reduce',27],'break':['reduce',27],'continue':['reduce',27],'assignOperators':['reduce',27],'callout':['reduce',27],'operadores':['reduce',27],'equalityOperators':['reduce',27],'conditionOperators':['reduce',27],'boolLiteral':['reduce',27],'charLiteral':['reduce',27],'stringLiteral':['reduce',27],'intLiteral':['reduce',27],'id':['reduce',27],'menos':['reduce',27],'!':['reduce',27],'menos':['reduce',27],'!':['reduce',27],'statementList':['reduce',27],'statement':['reduce',27],'location':['reduce',27],'methodCall':['reduce',27],'block':['reduce',27],'varDecl':['reduce',27],'expr':['reduce',27],'methodName':['reduce',27],'literal':['reduce',27],'-':['reduce',27],'!':['reduce',27],'=':['reduce',27],'listExp':['reduce',27],'binOp':['reduce',27],'calloutArgsL':['reduce',27],'argCallout':['reduce',27]},
            69:{'{':['reduce',19],'}':['reduce',19],',':['reduce',19],'[':['reduce',19],']':['reduce',19],';':['reduce',19],'type':['reduce',19],'void':['reduce',19],'if':['reduce',19],'(':['reduce',19],')':['reduce',19],'else':['reduce',19],'for':['reduce',19],'return':['reduce',19],'break':['reduce',19],'continue':['reduce',19],'assignOperators':['reduce',19],'callout':['reduce',19],'operadores':['reduce',19],'equalityOperators':['reduce',19],'conditionOperators':['reduce',19],'boolLiteral':['reduce',19],'charLiteral':['reduce',19],'stringLiteral':['reduce',19],'intLiteral':['reduce',19],'id':['reduce',19],'menos':['reduce',19],'!':['reduce',19],'menos':['reduce',19],'!':['reduce',19],'statementList':['reduce',19],'statement':['reduce',19],'location':['reduce',19],'methodCall':['reduce',19],'block':['reduce',19],'varDecl':['reduce',19],'expr':['reduce',19],'methodName':['reduce',19],'literal':['reduce',19],'-':['reduce',19],'!':['reduce',19],'=':['reduce',19],'listExp':['reduce',19],'binOp':['reduce',19],'calloutArgsL':['reduce',19],'argCallout':['reduce',19]},
            70:{'{':['reduce',28],'}':['reduce',28],',':['reduce',28],'[':['reduce',28],']':['reduce',28],';':['reduce',28],'type':['reduce',28],'void':['reduce',28],'if':['reduce',28],'(':['reduce',28],')':['reduce',28],'else':['reduce',28],'for':['reduce',28],'return':['reduce',28],'break':['reduce',28],'continue':['reduce',28],'assignOperators':['reduce',28],'callout':['reduce',28],'operadores':['reduce',28],'equalityOperators':['reduce',28],'conditionOperators':['reduce',28],'boolLiteral':['reduce',28],'charLiteral':['reduce',28],'stringLiteral':['reduce',28],'intLiteral':['reduce',28],'id':['reduce',28],'menos':['reduce',28],'!':['reduce',28],'menos':['reduce',28],'!':['reduce',28],'statementList':['reduce',28],'statement':['reduce',28],'location':['reduce',28],'methodCall':['reduce',28],'block':['reduce',28],'varDecl':['reduce',28],'expr':['reduce',28],'methodName':['reduce',28],'literal':['reduce',28],'-':['reduce',28],'!':['reduce',28],'=':['reduce',28],'listExp':['reduce',28],'binOp':['reduce',28],'calloutArgsL':['reduce',28],'argCallout':['reduce',28]},
            71:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'stringLiteral':['shift',79],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33],'calloutArgsL':['goTo',75],'argCallout':['goTo',77]},
            72:{'{':['reduce',7],'}':['reduce',7],',':['reduce',7],'[':['reduce',7],']':['reduce',7],';':['reduce',7],'type':['reduce',7],'void':['reduce',7],'if':['reduce',7],'(':['reduce',7],')':['reduce',7],'else':['shift',80],'for':['reduce',7],'return':['reduce',7],'break':['reduce',7],'continue':['reduce',7],'assignOperators':['reduce',7],'callout':['reduce',7],'operadores':['reduce',7],'equalityOperators':['reduce',7],'conditionOperators':['reduce',7],'boolLiteral':['reduce',7],'charLiteral':['reduce',7],'stringLiteral':['reduce',7],'intLiteral':['reduce',7],'id':['reduce',7],'menos':['reduce',7],'!':['reduce',7],'menos':['reduce',7],'!':['reduce',7],'statementList':['reduce',7],'statement':['reduce',7],'location':['reduce',7],'methodCall':['reduce',7],'block':['reduce',7],'varDecl':['reduce',7],'expr':['reduce',7],'methodName':['reduce',7],'literal':['reduce',7],'-':['reduce',7],'!':['reduce',7],'=':['reduce',7],'listExp':['reduce',7],'binOp':['reduce',7],'calloutArgsL':['reduce',7],'argCallout':['reduce',7]},
            73:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['goTo',24],'literal':['goTo',28],'-':['goTo',33]},
            74:{'{':['reduce',33],'{':['reduce',33],',':['reduce',33],'[':['reduce',33],']':['reduce',33],';':['reduce',33],'type':['reduce',33],'void':['reduce',33],'if':['reduce',33],'(':['reduce',33],')':['reduce',33],'else':['reduce',33],'for':['reduce',33],'return':['reduce',33],'break':['reduce',33],'continue':['reduce',33],'assignOperators':['reduce',33],'callout':['reduce',33],'operadores':['reduce',33],'equalityOperators':['reduce',33],'conditionOperators':['reduce',33],'boolLiteral':['reduce',33],'charLiteral':['reduce',33],'stringLiteral':['reduce',33],'intLiteral':['reduce',33],'id':['reduce',33],'menos':['reduce',33],'!':['reduce',33],'menos':['reduce',33],'!':['reduce',33],'statementList':['reduce',33],'statement':['reduce',33],'location':['reduce',33],'methodCall':['reduce',33],'block':['reduce',33],'varDecl':['reduce',33],'expr':['reduce',33],'methodName':['reduce',33],'literal':['reduce',33],'-':['reduce',33],'!':['reduce',33],'=':['reduce',33],'listExp':['reduce',33],'binOp':['reduce',33],'calloutArgsL':['reduce',33],'argCallout':['reduce',33]},
            75:{')':['shift',78]},
            76:{'{':['reduce',29],'{':['reduce',29],',':['reduce',29],'[':['reduce',29],']':['reduce',29],';':['reduce',29],'type':['reduce',29],'void':['reduce',29],'if':['reduce',29],'(':['reduce',29],')':['reduce',29],'else':['reduce',29],'for':['reduce',29],'return':['reduce',29],'break':['reduce',29],'continue':['reduce',29],'assignOperators':['reduce',29],'callout':['reduce',29],'operadores':['reduce',29],'equalityOperators':['reduce',29],'conditionOperators':['reduce',29],'boolLiteral':['reduce',29],'charLiteral':['reduce',29],'stringLiteral':['reduce',29],'intLiteral':['reduce',29],'id':['reduce',29],'menos':['reduce',29],'!':['reduce',29],'menos':['reduce',29],'!':['reduce',29],'statementList':['reduce',29],'statement':['reduce',29],'location':['reduce',29],'methodCall':['reduce',29],'block':['reduce',29],'varDecl':['reduce',29],'expr':['reduce',29],'methodName':['reduce',29],'literal':['reduce',29],'-':['reduce',29],'!':['reduce',29],'=':['reduce',29],'listExp':['reduce',29],'binOp':['reduce',29],'calloutArgsL':['reduce',29],'argCallout':['reduce',29]},
            77:{'{':['reduce',30],'}':['reduce',30],',':['shift',82],'[':['reduce',30],']':['reduce',30],';':['reduce',30],'type':['reduce',30],'void':['reduce',30],'if':['reduce',30],'(':['reduce',30],')':['reduce',30],'else':['reduce',30],'for':['reduce',30],'return':['reduce',30],'break':['reduce',30],'continue':['reduce',30],'assignOperators':['reduce',30],'callout':['reduce',30],'operadores':['reduce',30],'equalityOperators':['reduce',30],'conditionOperators':['reduce',30],'boolLiteral':['reduce',30],'charLiteral':['reduce',30],'stringLiteral':['reduce',30],'intLiteral':['reduce',30],'id':['reduce',30],'menos':['reduce',30],'!':['reduce',30],'menos':['reduce',30],'!':['reduce',30],'statementList':['reduce',30],'statement':['reduce',30],'location':['reduce',30],'methodCall':['reduce',30],'block':['reduce',30],'varDecl':['reduce',30],'expr':['reduce',30],'methodName':['reduce',30],'literal':['reduce',30],'-':['reduce',30],'!':['reduce',30],'=':['reduce',30],'listExp':['reduce',30],'binOp':['reduce',30],'calloutArgsL':['reduce',30],'argCallout':['reduce',30]},
            78:{'{':['reduce',34],'}':['reduce',34],',':['reduce',34],'[':['reduce',34],']':['reduce',34],';':['reduce',34],'type':['reduce',34],'void':['reduce',34],'if':['reduce',34],'(':['reduce',34],')':['reduce',34],'else':['reduce',34],'for':['reduce',34],'return':['reduce',34],'break':['reduce',34],'continue':['reduce',34],'assignOperators':['reduce',34],'callout':['reduce',34],'operadores':['reduce',34],'equalityOperators':['reduce',34],'conditionOperators':['reduce',34],'boolLiteral':['reduce',34],'charLiteral':['reduce',34],'stringLiteral':['reduce',34],'intLiteral':['reduce',34],'id':['reduce',34],'menos':['reduce',34],'!':['reduce',34],'menos':['reduce',34],'!':['reduce',34],'statementList':['reduce',34],'statement':['reduce',34],'location':['reduce',34],'methodCall':['reduce',34],'block':['reduce',34],'varDecl':['reduce',34],'expr':['reduce',34],'methodName':['reduce',34],'literal':['reduce',34],'-':['reduce',34],'!':['reduce',34],'=':['reduce',34],'listExp':['reduce',34],'binOp':['reduce',34],'calloutArgsL':['reduce',34],'argCallout':['reduce',34]},
            79:{'{':['reduce',35],'}':['reduce',35],',':['reduce',35],'[':['reduce',35],']':['reduce',35],';':['reduce',35],'type':['reduce',35],'void':['reduce',35],'if':['reduce',35],'(':['reduce',35],')':['reduce',35],'else':['reduce',35],'for':['reduce',35],'return':['reduce',35],'break':['reduce',35],'continue':['reduce',35],'assignOperators':['reduce',35],'callout':['reduce',35],'operadores':['reduce',35],'equalityOperators':['reduce',35],'conditionOperators':['reduce',35],'boolLiteral':['reduce',35],'charLiteral':['reduce',35],'stringLiteral':['reduce',35],'intLiteral':['reduce',35],'id':['reduce',35],'menos':['reduce',35],'!':['reduce',35],'menos':['reduce',35],'!':['reduce',35],'statementList':['reduce',35],'statement':['reduce',35],'location':['reduce',35],'methodCall':['reduce',35],'block':['reduce',35],'varDecl':['reduce',35],'expr':['reduce',35],'methodName':['reduce',35],'literal':['reduce',35],'-':['reduce',35],'!':['reduce',35],'=':['reduce',35],'listExp':['reduce',35],'binOp':['reduce',35],'calloutArgsL':['reduce',35],'argCallout':['reduce',35]},
            80:{'{':['shift',1],'block':['goTo',83]},
            81:{'{':['shift',1],'block':['goTo',84]},
            82:{'!':['shift',34],'(':['shift',35],'callout':['shift',16],'boolLiteral':['shift',31],'charLiteral':['shift',30],'stringLiteral':['shift',79],'intLiteral':['shift',29],'stringLiteral':['shift',29],'id':['shift',15],'location':['goTo',26],'methodCall':['goTo',27],'expr':['goTo',32],'methodName':['shift',24],'literal':['goTo',28],'-':['goTo',33],'calloutArgsL':['goTo',85],'argCallout':['goTo',77]},
            83:{'{':['reduce',8],'}':['reduce',8],',':['reduce',8],'[':['reduce',8],']':['reduce',8],';':['reduce',8],'type':['reduce',8],'void':['reduce',8],'if':['reduce',8],'(':['reduce',8],')':['reduce',8],'else':['reduce',8],'for':['reduce',8],'return':['reduce',8],'break':['reduce',8],'continue':['reduce',8],'assignOperators':['reduce',8],'callout':['reduce',8],'operadores':['reduce',8],'equalityOperators':['reduce',8],'conditionOperators':['reduce',8],'boolLiteral':['reduce',8],'charLiteral':['reduce',8],'stringLiteral':['reduce',8],'intLiteral':['reduce',8],'id':['reduce',8],'menos':['reduce',8],'!':['reduce',8],'menos':['reduce',8],'!':['reduce',8],'statementList':['reduce',8],'statement':['reduce',8],'location':['reduce',8],'methodCall':['reduce',8],'block':['reduce',8],'varDecl':['reduce',8],'expr':['reduce',8],'methodName':['reduce',8],'literal':['reduce',8],'-':['reduce',8],'!':['reduce',8],'=':['reduce',8],'listExp':['reduce',8],'binOp':['reduce',8],'calloutArgsL':['reduce',8],'argCallout':['reduce',8]},
            84:{'{':['reduce',9],'}':['reduce',9],',':['reduce',9],'[':['reduce',9],']':['reduce',9],';':['reduce',9],'type':['reduce',9],'void':['reduce',9],'if':['reduce',9],'(':['reduce',9],')':['reduce',9],'else':['reduce',9],'for':['reduce',9],'return':['reduce',9],'break':['reduce',9],'continue':['reduce',9],'assignOperators':['reduce',9],'callout':['reduce',9],'operadores':['reduce',9],'equalityOperators':['reduce',9],'conditionOperators':['reduce',9],'boolLiteral':['reduce',9],'charLiteral':['reduce',9],'stringLiteral':['reduce',9],'intLiteral':['reduce',9],'id':['reduce',9],'menos':['reduce',9],'!':['reduce',9],'menos':['reduce',9],'!':['reduce',9],'statementList':['reduce',9],'statement':['reduce',9],'location':['reduce',9],'methodCall':['reduce',9],'block':['reduce',9],'varDecl':['reduce',9],'expr':['reduce',9],'methodName':['reduce',9],'literal':['reduce',9],'-':['reduce',9],'!':['reduce',9],'=':['reduce',9],'listExp':['reduce',9],'binOp':['reduce',9],'calloutArgsL':['reduce',9],'argCallout':['reduce',9]},
            85:{'{': ['reduce', 31], '}': ['reduce', 31], ',': ['reduce', 31], '[': ['reduce', 31], ']': ['reduce', 31], ';': ['reduce', 31], 'type': ['reduce', 31], 'void': ['reduce', 31], 'if': ['reduce', 31], '(': ['reduce', 31], ')': ['reduce', 31], 'else': ['reduce', 31], 'for': ['reduce', 31], 'return': ['reduce', 31], 'break': ['reduce', 31], 'continue': ['reduce', 31], 'assignOperators': ['reduce', 31], 'callout': ['reduce', 31], 'operadores': ['reduce', 31], 'equalityOperators': ['reduce', 31], 'conditionOperators': ['reduce', 31], 'boolLiteral': ['reduce', 31], 'charLiteral': ['reduce', 31], 'stringLiteral': ['reduce', 31], 'intLiteral': ['reduce', 31], 'id': ['reduce', 31], 'menos': ['reduce', 31], '!': ['reduce', 31], 'menos': ['reduce', 31], '!': ['reduce', 31], 'statementList': ['reduce', 31], 'statement': ['reduce', 31], 'location': ['reduce', 31], 'methodCall': ['reduce', 31], 'block': ['reduce', 31], 'varDecl': ['reduce', 31], 'expr': ['reduce', 31], 'methodName': ['reduce', 31], 'literal': ['reduce', 31], '-': ['reduce', 31], '!': ['reduce', 31], '=': ['reduce', 31], 'listExp': ['reduce', 31], 'binOp': ['reduce', 31], 'calloutArgsL': ['reduce', 31], 'argCallout': ['reduce', 31]},
            86:{'{':['reduce',11],'}':['reduce',11],',':['reduce',11],'[':['reduce',11],']':['reduce',11],';':['reduce',11],'type':['reduce',11],'void':['reduce',11],'if':['reduce',11],'(':['reduce',11],')':['reduce',11],'else':['reduce',11],'for':['reduce',11],'return':['reduce',11],'break':['reduce',11],'continue':['reduce',11],'assignOperators':['reduce',11],'callout':['reduce',11],'operadores':['reduce',11],'equalityOperators':['reduce',11],'conditionOperators':['reduce',11],'boolLiteral':['reduce',11],'charLiteral':['reduce',11],'stringLiteral':['reduce',11],'intLiteral':['reduce',11],'id':['reduce',11],'menos':['reduce',11],'!':['reduce',11],'menos':['reduce',11],'!':['reduce',11],'statementList':['reduce',11],'statement':['reduce',11],'location':['reduce',11],'methodCall':['reduce',11],'block':['reduce',11],'varDecl':['reduce',11],'expr':['reduce',11],'methodName':['reduce',11],'literal':['reduce',11],'-':['reduce',11],'!':['reduce',11],'=':['reduce',11],'listExp':['reduce',11],'binOp':['reduce',11],'calloutArgsL':['reduce',11],'argCallout':['reduce',11]},
            87:{'{':['reduce',19],'}':['reduce',19],',':['reduce',19],'[':['reduce',19],']':['reduce',19],';':['reduce',19],'type':['reduce',19],'void':['reduce',19],'if':['reduce',19],'(':['reduce',19],')':['reduce',19],'else':['reduce',19],'for':['reduce',19],'return':['reduce',19],'break':['reduce',19],'continue':['reduce',19],'assignOperators':['reduce',19],'callout':['reduce',19],'operadores':['reduce',19],'equalityOperators':['reduce',19],'conditionOperators':['reduce',19],'boolLiteral':['reduce',19],'charLiteral':['reduce',19],'stringLiteral':['reduce',19],'intLiteral':['reduce',19],'id':['reduce',19],'menos':['reduce',19],'!':['reduce',19],'menos':['reduce',19],'!':['reduce',19],'statementList':['reduce',19],'statement':['reduce',19],'location':['reduce',19],'methodCall':['reduce',19],'block':['reduce',19],'varDecl':['reduce',19],'expr':['reduce',19],'methodName':['reduce',19],'literal':['reduce',19],'-':['reduce',19],'!':['reduce',19],'=':['reduce',19],'listExp':['reduce',19],'binOp':['reduce',19],'calloutArgsL':['reduce',19],'argCallout':['reduce',19]}
     }

    def fieldParse(self, Program, nodoPrinc, tipoDFA, debug, listaErrores):
        lista = nodoPrinc.lista
        # print(nodoPrinc.tipo)
        if tipoDFA == 'listaFieldDecl' :
            listaNodos0 = []
            contBsN = 0
            listacontB = []
            
            for nodo in lista:
                if nodo.objNodo.simb.name == ';' :
                    listacontB.append(contBsN)
                contBsN += 1          
            
            listaField = []
            for split in range(len(listacontB)) :
                if split == 0 :
                    listaField.append(lista[0:listacontB[split] + 1])
                else:
                    listaField.append(lista[listacontB[split - 1] + 1:listacontB[split] + 1])
            
            for fieldDecl in listaField:
                if len(fieldDecl) < 3 :
                    listaErrores.append("Parse error: No hay suficientes tokens en la declaracion! linea - " + str(fieldDecl[0].objNodo.line))
                if len(fieldDecl) == 3 :
                    if fieldDecl[0].objNodo.simb.name != 'type' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[0].objNodo.simb.name + " linea - " + str(fieldDecl[0].objNodo.line))
                    if fieldDecl[1].objNodo.simb.name != 'id' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[1].objNodo.simb.name + " linea - " + str(fieldDecl[1].objNodo.line))
                    if fieldDecl[2].objNodo.simb.name != ';' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[2].objNodo.simb.name + " linea - " + str(fieldDecl[2].objNodo.line))
                    if fieldDecl[0].objNodo.simb.name == 'type' and fieldDecl[1].objNodo.simb.name == 'id' and fieldDecl[2].objNodo.simb.name == ';' :
                        objField = field.FieldDecl()
                        listaNodos0.append(nodoA.Nodo(objField, "fieldDecl", [fieldDecl[0], fieldDecl[1], fieldDecl[2]]))
                
                if len(fieldDecl) > 3 :
                    idField = []
                    idSeguir = True
                    if fieldDecl[0].objNodo.simb.name != 'type' :
                        listaErrores.append("Parse error: Token inesperado " + fieldDecl[0].objNodo.simb.name + " linea - " + str(fieldDecl[0].objNodo.line))
                        idSeguir = False
                    for i in range(1, len(fieldDecl)-1):
                        if i % 2 != 0:
                            if fieldDecl[i].objNodo.simb.name != 'id' :
                                listaErrores.append("Parse error: Token inesperado " + fieldDecl[i].objNodo.simb.name + " linea - " + str(fieldDecl[i].objNodo.line))
                                idSeguir = False
                            else:
                                idField.append(fieldDecl[i])
                        else:
                            if fieldDecl[i].objNodo.simb.name != ',' :
                                listaErrores.append("Parse error: Token inesperado " + fieldDecl[i].objNodo.simb.name + " linea - " + str(fieldDecl[i].objNodo.line))
                                idSeguir = False
                    if idSeguir :
                        for i in idField:
                            objField = field.FieldDecl()
                            listaNodos0.append(nodoA.Nodo(objField, "fieldDecl", [fieldDecl[0], i, fieldDecl[len(fieldDecl)-1]]))

            nodoPrinc.lista = listaNodos0
            Program.lista[3] = nodoPrinc

        if debug :
            print("Lista Errores", listaErrores)

    def metParse(self, Program, nodoPrinc, tipoDFA, debug, listaErrores):
        listaMethod = []
        lista = nodoPrinc.lista

        if len(lista) < 6 :
            listaErrores.append("Parse error: Not enough tokens to parse a valid method decl")
        else:
            if lista[0].objNodo.simb.name != "type" and lista[0].objNodo.simb.name != "void" :
                listaErrores.append("Parse error: Token inesperado "+ lista[0].objNodo.simb.name + " linea - " + str(lista[0].objNodo.line))
            if lista[1].objNodo.simb.name != "id" :
                listaErrores.append("Parse error: Token inesperado "+ lista[1].objNodo.simb.name + " linea - " + str(lista[1].objNodo.line))
            if lista[2].objNodo.simb.name != "(" :
                listaErrores.append("Parse error: Token inesperado "+ lista[2].objNodo.simb.name + " linea - " + str(lista[2].objNodo.line))
            
            for indexsN in range(len(lista)) :
                if indexsN < (len(lista) - 3) :
                    if (lista[indexsN].objNodo.simb.name == "type" or lista[indexsN].objNodo.simb.name == "void") and lista[indexsN+1].objNodo.simb.name == "id" and lista[indexsN+2].objNodo.simb.name == "(" :
                        
                        # Nodo method 
                        metodoObj = metodo.MethodDecl()
                        metodoNodo = nodoA.Nodo(metodoObj, "methodDecl", [lista[indexsN], lista[indexsN + 1], lista[indexsN + 2]])
                        listaMethod.append(metodoNodo)

                        countM = indexsN + 3
                        varHijo = []
                        seguir = True
                        while lista[countM].objNodo.simb.name != ")" and countM < (len(lista) - 3):
                            seguir = True
                            if lista[countM].objNodo.simb.name == "type" :
                                if lista[countM+1].objNodo.simb.name != "id" or (lista[countM+2].objNodo.simb.name != "," and lista[countM+2].objNodo.simb.name != ")") :
                                    listaErrores.append("Parse error: Token inesperado " + lista[countM].objNodo.simb.name + " linea - " + str(lista[countM].objNodo.line))
                                    seguir = False
                                else:
                                    varHijo.append(lista[countM])

                            elif lista[countM].objNodo.simb.name == "id" :
                                if (lista[countM+1].objNodo.simb.name != "," and lista[countM+1].objNodo.simb.name != ")") or lista[countM-1].objNodo.simb.name != "type" :
                                    listaErrores.append("Parse error: Token inesperado " + lista[countM].objNodo.simb.name + " linea - " + str(lista[countM].objNodo.line))
                                    seguir = False
                                else:
                                    varHijo.append(lista[countM])

                            elif lista[countM].objNodo.simb.name == "," :
                                if lista[countM+1].objNodo.simb.name != "type" or lista[countM-1].objNodo.simb.name != "id" :
                                    listaErrores.append("Parse error: Token inesperado "+ lista[countM].objNodo.simb.name + " linea - " + str(lista[countM].objNodo.line))
                                    seguir = False
                                else:
                                    varHijo.append(lista[countM])
                            else:
                                listaErrores.append("Parse error: Token inesperado "+ lista[countM].objNodo.simb.name + " linea - " + str(lista[countM].objNodo.line))
                                seguir = False
                            countM += 1

                        if lista[countM].objNodo.simb.name != ")" :
                            listaErrores.append("Parse error: Falta ) en la declaracion del metodo")
                        varObj = listaVariables.VarDeclList()
                        varNodo = nodoA.Nodo(varObj, "listaVarDecl", [])
                        if seguir :
                            varNodo.lista = varHijo
                        metodoNodo.lista.append(varNodo)
                        metodoNodo.lista.append(lista[countM])
                        countM += 1
                        
                        blockHijos = []
                        if lista[countM].objNodo.simb.name == "{" :
                                while not((lista[countM].objNodo.simb.name == "type" or lista[countM].objNodo.simb.name == "void") and lista[countM+1].objNodo.simb.name == "id" and lista[countM+2].objNodo.simb.name == "(") and countM<len(lista)-2:
                                    blockHijos.append(lista[countM])
                                    countM+=1
                                if countM==len(lista)-2 :
                                    blockHijos.append(lista[countM])
                                    blockHijos.append(lista[countM+1])                              

                        # Nodo block
                        blockObj = block.Block()
                        blockNodo = nodoA.Nodo(blockObj, "block", blockHijos)
                        metodoNodo.lista.append(blockNodo)

            nodoPrinc.lista = listaMethod
        if debug:
            print(listaErrores)

    def blockParse(self, Program, nodoPrinc, debug, listaErrores):
        nodoPrincipal = nodoA.Nodo("$", "$", [])
        states = [0]
        stackNodos = [nodoPrincipal]

        revisarLista = nodoPrinc.lista
        
        tamanoRev = len(revisarLista)
        contB = 0
        ultEstado = states[-1]
        parametros = []
        nodoActual = revisarLista[ultEstado]
        parametros = self.dfa.get(ultEstado).get(nodoActual.tipo)
        if parametros==None :
            listaErrores.append("Parse error: Falta { linea - " + str(nodoActual.objNodo.line))

        contWhile = 0
        while contB < tamanoRev and contWhile < 15 :
            if parametros != None :
                if parametros[0] == 'shift' :
                    stackNodos.append(nodoActual)
                    states.append(parametros[1])
                    contB += 1
                    nodoActual = revisarLista[contB]
                    parametros = self.dfa.get(states[-1]).get(nodoActual.tipo)

                elif parametros[0] == 'goTo' :
                    states.append(parametros[1])
                    nodoActual = revisarLista[contB]
                    parametros = self.dfa.get(states[-1]).get(nodoActual.tipo)

                elif parametros[0] == 'reduce' :

                    if parametros[1] == 2 :  
                        listaTemporal = []
                        abrirStatement = ""
                        for verNodo in stackNodos[::-1]:
                            if verNodo.tipo == "statement" :
                                listaTemporal.append(verNodo)
                            elif verNodo.tipo == "{" :
                                abrirStatement = verNodo
                                break
                            else:
                                listaErrores.append("Parsing error, Elemento inesperado " + verNodo.tipo)
                                break

                        statementNodos = nodoA.Nodo("statementList", "statementList", listaTemporal[::-1])
                        blockNodo = nodoA.Nodo("block", "block", [abrirStatement, statementNodos, revisarLista[contB]])
                        count = len(listaTemporal) + 1
                        stackNodos = stackNodos[:-count]
                        states = states[:-(count)]
                        stackNodos.append(blockNodo)
                        contB += 1

                        parametros = self.dfa.get(states[-1]).get(blockNodo.tipo)

                    else:
                        objNodo = list(self.gramatica[parametros[1]-1].keys())[0]
                        tipo = list(self.gramatica[parametros[1]-1].keys())[0]
                        count = len(list(self.gramatica[parametros[1]-1].values())[0])

                        listaHijos = stackNodos[-count:]

                        stackNodos = stackNodos[:-count]

                        states = states[:-(count)]
                        nuevoN = nodoA.Nodo(objNodo, tipo, listaHijos)

                        stackNodos.append(nuevoN)
                        parametros = self.dfa.get(states[-1]).get(nuevoN.tipo)

                        if parametros != None and parametros[0] == 'goTo' and parametros[1] == 32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "!" :
                                parametros = ['goTo', 58]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "menos" and stackNodos[-3].tipo != "expr" :
                                parametros = ['goTo', 58]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if revisarLista[contB].tipo == "{" and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "," and stackNodos[-3].tipo == "expr" :
                                parametros = ['goTo', 81]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if revisarLista[contB].tipo == ")" and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "(" and stackNodos[-3].tipo != "if" :
                                parametros = ['goTo', 59]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "menos" and stackNodos[-3].tipo == "expr" :
                                parametros = ['goTo', 69]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "binOp" and stackNodos[-3].tipo == "expr" :
                                parametros = ['goTo', 69]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if revisarLista[contB].tipo == ")" and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "(" and stackNodos[-3].tipo == "if" :
                                parametros = ['goTo', 44]

                        if parametros!=None and parametros[0]=='goTo' and parametros[1]==32 :
                            if revisarLista[contB].tipo == "," and stackNodos[-1].tipo == "expr" and stackNodos[-2].tipo == "assignOperators" :
                                parametros = ['goTo', 65]

                elif parametros[0]=='accept' :
                    print("Aceptado!")
            else:
                # Estado no definido
                if contB<len(revisarLista):
                    listaErrores.append("Parse error: Token inesperado " + revisarLista[contB].tipo + " linea - " + str(revisarLista[contB].objNodo.line))
                else:
                    listaErrores.append("Parse error: Token inesperado " + revisarLista[contB-1].tipo + " linea - " + str(revisarLista[contB-1].objNodo.line))
                break

        if debug :
            print(listaErrores)

        if len(listaErrores) == 0 :
            return stackNodos[-1]
        else:
            return nodoA.Nodo("block", "block", [])
    
    def accepts(self, listaTokens):
        state = 0
        contAccepts = 0
        parametros=[]

        print(len(listaTokens))

        tokenActual = listaTokens[contAccepts].simb.name
        parametros = self.dfa.get(state).get(tokenActual)

        print(parametros)

        while contAccepts <= len(listaTokens) :
            #print(listaTokens[contAccepts].simb.name)
            print(state)
            if parametros != None :
                if parametros[0] == 'shift' :
                    tokenActual = listaTokens[contAccepts].simb.name
                    self.tokens.append(tokenActual)
                    parametros = self.dfa.get(self.states[-1]).get(tokenActual)
                    self.states.append(parametros[1])
                    contAccepts += 1

                    if contAccepts < len(listaTokens) :
                        tokenActual = listaTokens[contAccepts].simb.name
                    parametros = self.dfa.get(self.states[-1]).get(tokenActual)
                    print("shift")

                elif parametros[0] == 'goTo' :
                    print(tokenActual)
                    print(parametros[1])
                    self.states.append(parametros[1])
                    
                    if contAccepts < len(listaTokens) :
                        tokenActual = listaTokens[contAccepts].simb.name
                        parametros = self.dfa.get(self.states[-1]).get(tokenActual)
                    else:
                        print(parametros)
                        self.tokens.pop(-1)
                        self.states.pop(-1)
                        break
                    print('goTo')
                
                elif parametros[0] == 'reduce' :
                    print(parametros[1])
                    node = nodoA.Nodo(list(self.gramaticaProgram[parametros[1]-1].keys())[0], list(self.gramaticaProgram[parametros[1]-1].values())[0])
                    count = len(list(self.gramaticaProgram[parametros[1]-1].values())[0])
                    self.tokens = self.tokens[:-count]
                    self.states = self.states[:-(count)]
                    self.tokens.append(list(self.gramaticaProgram[parametros[1]-1].keys())[0])
                    tokenActual = self.tokens[-1]
                    print(self.states)
                    parametros = self.dfa.get(self.states[-1]).get(tokenActual)

                    print("Lista nodos", node.listaTokens)
                    print("Nodo - ", node)
                    print("reduce")

                elif parametros[0] == 'accept' :
                    print("Acepatdo!")
            else:
                print("Estado no definido")
                if contAccepts < len(listaTokens) :
                    print("Token inesperado",listaTokens[contAccepts].simb.name," linea - ",listaTokens[contAccepts].line)
                else:
                    print("Token inesperado",listaTokens[contAccepts-1].simb.name," linea - ",listaTokens[contAccepts-1].line)
                break
            print(self.tokens)
            print(self.states)
            print("------")

        print(self.states)
        print(self.tokens)
        if(len(self.tokens)==1 and len(self.states)==1):
            print("Parseo Completo")
        else:
            print("Parseo Invalido")
        return True