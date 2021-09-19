from datetime import datetime
# Para poner la fecha en el nombre

class OutputFile():

    def outputFile(self, tokens, nombreArchivoOut):
        archivoSalida = open("outputs/" + nombreArchivoOut + ".txt", "w")

        for token in tokens:
            archivoSalida.write(token+"\n")
        
        archivoSalida.close()
