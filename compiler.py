# CLI
import scanner.Scanner as scanner
import files.inputFile as inputFile
import files.outputFile as outputFile
import parser1.Parser as parser
import semantic.Semantic as semantic
import irt.Irt as Irt
import codeG.Codegen as Codegen
from anytree import RenderTree


import sys

# Help -h
def ayuda():
     print("\n\nAyuda: ")
     print("-o <outname> ")
     print("• Escribir el output a <outname>")

     print("\n-target <stage> ")
     print("• Es uno de los siguientes elementos: scan, parse, ast, semantic, irt, codegen")

     print("\n-opt <opt_stage> ")
     print("• Es uno de: constant, algebraic;")
     
     print("\n-debug <stage> ")
     print("• Imprime información de debugging\n\n")
     

def execute(inputCodigo, nombreArchivoOut, stage, optStage, debugStage):
    #opciones
    if stage == "scanner" or stage == "parser" or stage == "" or stage=="semantic" or stage=="irt" or stage == "codegen":
        debug = False
        #debug
        if "scanner" in debugStage:
            debug = True

        inp = inputFile.inputFile()
        #scanner y leer tokens inputFile
        leerArchivo = inp.convertirArchivo(inputCodigo)
        print("\n\n ----------------------------")

        scan = scanner.Scanner()
        listaTokens, listaErrores = scan.scanner(leerArchivo, debug)

        printTokens = []
        
        if optStage == "constant":
            printTokens.append("optimizing: constant folding")
        if optStage == "algebraic":
            printTokens.append("optimizing: algebraic simplification")

        for token in listaTokens:
            printTokens.append(token.prettyPrint())
        
        # Generar output
        out = outputFile.OutputFile()
        out.outputFile(printTokens, nombreArchivoOut)

        ErrS = len(listaErrores)
        
        for error in listaErrores:
            print(error)

        print("\n ----------------------------")
    
    if stage == "parser" or stage=="semantic" or stage=="irt" or stage == "codegen" or stage == "":
        debug = False
        #debug
        if "parser" in debugStage :
            debug = True
    
        parse = parser.Parser()

        mainProgram, listaErrores = parse.parser(listaTokens, debug)

        # Generar output
        out.outputFile(listaErrores, str(nombreArchivoOut+"Parse"))

        ErrP = len(listaErrores)

    if stage=="semantic" or stage=="irt" or stage == "codegen" or stage == "":
        debug = False

        if("semantic" in debugStage):
            debug = True

        smtic = semantic.Semantic()
        listaErrores = smtic.semantic(mainProgram, debug)
        
        # Generar output
        out.outputFile(listaErrores, str(nombreArchivoOut+"Semantic"))

        ErrSM = len(listaErrores)
        print("\n ----------------------------")

    #
    if stage == "irt" or stage == "codegen" or stage == "":
        print("\nIRT--------")
        if ErrS == 0 and ErrP == 0 and ErrSM == 0:
            debug = False
            if "irt" in debugStage:
                debug = True
            irt = Irt.Irt()
            listaIrt = irt.irt(mainProgram, debug)
            # out.outputFile(listaIrt, str(nombreArchivoOut+"Irt"))            

        else:
            print("Hay errores en el error_log")

    if stage == "codegen" or stage == "":
        print("\nCODE GENERATION--------")
        if ErrS == 0 and ErrP == 0 and ErrSM == 0:
            codegen = Codegen.Codegen()
            listaCod = codegen.codegen(mainProgram, debug, nombreArchivoOut)
            print(listaCod)
            # out.outputFile(listaCod, str(nombreArchivoOut+"CodeGen"))            
        else:
            print("Hay errores en el error_log")
        print("\n ----------------------------")

if __name__ == "__main__":
    inputCodigo = ""    # file de entrada
    nombreArchivo = ""  # nombre del archivo output
    stage = ""          # Scanner, Parse ...
    optStage = ""       # Constant / Algebraic
    debugStage = []     # Ahora solo es una fase cambiar a otra cosa
    
    if (len(sys.argv) >= 4) and (len(sys.argv) % 2 == 0):
        valido = True
        inputCodigo = sys.argv[1]
        for i in range(2, len(sys.argv)):
            if(i % 2 == 0): # los pares son los tag
                if(sys.argv[i] == '-o'):
                    nombreArchivo = sys.argv[i+1]
                elif(sys.argv[i] == '-target'):
                    stage = (sys.argv[i+1])
                elif(sys.argv[i] == '-opt'):
                    optStage = sys.argv[i+1]
                elif(sys.argv[i] == '-debug'):
                    debugStage = sys.argv[i+1].split(":")
                else:
                    valido = False
                    print('invalid param')
                    ayuda()
        if valido:
            execute(inputCodigo, nombreArchivo, stage, optStage, debugStage)

    elif len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            ayuda()
        else:
            inputCodigo = sys.argv[1]
            execute(inputCodigo, nombreArchivo, stage, optStage, debugStage)
    else:
        ayuda()



