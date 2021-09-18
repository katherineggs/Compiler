class Tokens:
    def __init__(self, tipoSimbolo, value=""):
        self.tipoSimbolo = tipoSimbolo
        self.value = value

    def prettyPrint(self):
        prettyPrint = "- Type: " + self.tipoSimbolo.name 
        if(self.value != ""):
            prettyPrint += ", Value: " + self.value+" -"
        else:
            prettyPrint += " -"
        return prettyPrint