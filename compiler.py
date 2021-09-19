# CLI
import scanner.Scanner as scanner
import files.inputFile as inputFile

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
     

def execute(inputCodigo, nombreArchivo, stage, optStage, debugStage):
    #opciones
    if(stage == "scanner"):
        print("prueba ss")
        debug = False
        #debug
        if(("scannner" in debugStage)):
            debug = True

        #scanner y leer tokens inputFile
        leerArchivo = inputFile.inputFile.convertirArchivo(inputCodigo)
        print("\n\n ------------------------")
        print(leerArchivo)

        listaTokens, ListaErrores = scanner.Scanner.scanner(leerArchivo, debug)
        printTokens = []

        for token in listaTokens:
            printTokens.append(token.prettyPrint())
    
    print(inputCodigo, nombreArchivo, stage, optStage, debugStage)

        #Generar output
        # --------------------------- Falta, ESCRIBIR ARCHIVO ---------------------------------------------


    
if __name__ == "__main__":
    inputCodigo = "/Users/andreareyes/Desktop/compiladores/Compiler/codigo.decaf"
    nombreArchivo = "out"
    stage = "scanner"
    optStage = ""
    debugStage = []
    
    if (len(sys.argv) >= 4 and len(sys.argv) % 2 == 0):
        valido = True
        print("file: " + sys.argv[0])
        print("<filename>: " + sys.argv[1])
        inputCodigo = sys.argv[1]
        for i in range(2, len(sys.argv)):
            if(i % 2 == 0):
                if(sys.argv[i] == '-o'):
                    nombreArchivo = sys.argv[i+1]
                elif(sys.argv[i] == '-target'):
                    stage = (sys.argv[i+1])
                elif(sys.argv[i] == '-opt'):
                    optStage = sys.argv[i+1]
                elif(sys.argv[i] == '-debug'):
                    string_stages = sys.argv[i+1].split(":")
                    debugStage = string_stages
                else:
                    valido = False
                    print('invalid param')
                    ayuda()
        print(stage)
        if(valido):
            execute(inputCodigo, nombreArchivo, stage, optStage, debugStage)

    elif (len(sys.argv) == 2):
        inputCodigo = sys.argv[1]
        execute(inputCodigo, nombreArchivo, stage, optStage, debugStage)
    else:
        ayuda()

execute("\n\n/Users/andreareyes/Desktop/compiladores/Compiler/codigo.decaf", "out", "parse", "", [])


