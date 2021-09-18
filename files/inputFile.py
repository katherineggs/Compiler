
def convertirArchivo(nombreArchivo):
    archivoString = []

    try:
        with open(nombreArchivo, "rb") as archivo:
            code = archivo.read().decode('ISO-8859-1')
    except FileNotFoundError:
        print("Error, archivo no encontrado")

    else:
        comentarios = False
        contador = 1

        for linea in code.split():
            #print("linea",linea)
            if("//" in linea and comentarios==False):
                lineaToString = linea.replace(linea[linea.find("//"):-1], "")
                lineaToString = ' '.join(lineaToString.split())

                if(lineaToString != ""):
                    archivoString.append([lineaToString, contador])
            
            elif("/*" in linea):
                comentarios = True
            elif("*/" in linea):
                comentarios = False
            elif(comentarios==False):
                lineaToString = linea
                cont = 0
                for caracter in lineaToString:
                    if(caracter == "+" or caracter == "=" or caracter == "-" or caracter == "<" or caracter == ">" or caracter == "!"):
                        try:
                            if(caracter=='+'):
                                if(lineaToString[cont - 1] != '+'):
                                    lineaToString = lineaToString[:cont] + " " + lineaToString[cont] + lineaToString[cont + 1:]
                                    cont = cont+1

                                if(lineaToString[cont+1] != '+' and lineaToString[cont+1] != '='):
                                    lineaToString = lineaToString[:cont] + lineaToString[cont] + " " + lineaToString[cont + 1:]
                                    cont = cont + 1

                            if(caracter=='='):
                                    if(lineaToString[cont-1] != '=' and lineaToString[cont-1] != '+' and lineaToString[cont-1] != '-' and lineaToString[cont-1] != '<' and lineaToString[cont-1] != '>' and lineaToString[cont-1] != '!'):
                                        lineaToString = lineaToString[:cont] + " " + lineaToString[cont] + lineaToString[cont + 1:]
                                        cont = cont+ 1

                                    if(lineaToString[cont+1] != '='):
                                        lineaToString  = lineaToString[:cont] + lineaToString[cont] + " " + lineaToString[cont + 1:]
                                        cont = cont+1  

                            if(caracter=='-'):
                                    if(lineaToString[cont-1] != '-'):
                                        lineaToString = lineaToString[:cont] + " " + lineaToString[cont] + lineaToString[cont + 1:]
                                        cont = cont+1 
                                    if(lineaToString[cont+1] != '-' and lineaToString[cont+1] != '='):
                                        lineaToString = lineaToString[:cont] + lineaToString[cont] + " " + lineaToString[cont + 1:]
                                        cont = cont+1 

                            if(caracter=='<'):
                                lineaToString = lineaToString[:cont] + " " + lineaToString[cont] + lineaToString[cont + 1:]
                                cont = cont+1 

                                if(lineaToString[cont+1] != '='):
                                    lineaToString = lineaToString[:cont] + lineaToString[cont] + " " + lineaToString[cont + 1:]
                                    cont = cont+1 

                            if(caracter=='>'):
                                lineaToString = lineaToString[:cont] + " " + lineaToString[cont] + lineaToString[cont + 1:]
                                cont = cont+1 

                                if(lineaToString[cont+1] != '='):
                                    lineaToString = lineaToString = lineaToString[:cont] + lineaToString[cont] + " " + lineaToString[cont + 1:]
                                    cont = cont+1 

                            if(caracter=='!'): 
                                lineaToString = lineaToString[:cont] + " " + lineaToString[cont] + lineaToString[cont + 1:]
                                cont = cont+1 

                                if(lineaToString[cont+1] != '='):
                                    lineaToString = lineaToString[:cont] + lineaToString[cont] + " " + lineaToString[cont + 1:]
                                    cont = cont+1 

                        except Exception:
                            print(Exception)
                        else:
                            pass
                    
                    cont = cont+1

                for caracter in lineaToString:
                    if(caracter=="%" or caracter=="/"
                            or caracter=="*" or caracter=="(" or caracter==")" or caracter=="{" or caracter=="}" or caracter==";" or caracter==","):
                            lineaToString = lineaToString.replace(lineaToString[lineaToString.index(caracter)], " "+lineaToString[lineaToString.index(caracter)]+" ")
                        
                if("+=" in lineaToString):
                        lineaToString = lineaToString.replace("+=", " += ")
                elif("==" in lineaToString):
                    lineaToString = lineaToString.replace("==", " == ")
                elif("-=" in lineaToString):
                    lineaToString = lineaToString.replace("-=", " -= ")                    
                elif("<=" in lineaToString):
                    lineaToString = lineaToString.replace("<=", " <= ")  
                elif(">=" in lineaToString):
                    lineaToString = lineaToString.replace(">=", " >= ")  
                elif("!=" in lineaToString):
                    lineaToString = lineaToString.replace("!=", " != ")  
                elif("||" in lineaToString):
                    lineaToString = lineaToString.replace("||", " || ")  
                elif("&&" in lineaToString):
                    lineaToString = lineaToString.replace("&&", " && ")  
                elif("++" in lineaToString):
                    lineaToString = lineaToString.replace("++", " ++ ")
                elif("--" in lineaToString):
                    lineaToString = lineaToString.replace("--", " -- ")
                lineaToString = ' '.join(lineaToString.split())
                if(lineaToString!=""):
                    archivoString.append([lineaToString, contador])
            
            contador = contador + 1

        archivo.close()
        if(comentarios==True):
            archivoString = []
            print("Error, está mal comentareado")
    return archivoString
                    
hola = convertirArchivo("/Users/andreareyes/Desktop/compiladores/prueba-proyecto/inputs/prueba.decaf")
print(hola)



