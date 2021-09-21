# CLI
import scanner.Scanner as scanner
import files.inputFile as inputFile
import files.outputFile as outputFile

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
    if stage == "scanner" :
        debug = False
        #debug
        if "scanner" == debugStage :
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
        
        for error in listaErrores:
            print(error)

        print("\n ----------------------------")

if __name__ == "__main__":
    inputCodigo = ""    # file de entrada
    nombreArchivo = ""  # nombre del archivo output
    stage = ""          # Scanner, Parse ...
    optStage = ""       # Constant / Algebraic
    debugStage = ""     # Ahora solo es una fase cambiar a otra cosa
    
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
                    debugStage = sys.argv[i+1]
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



