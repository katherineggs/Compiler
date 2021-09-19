import abstracts.Symbols as Symbols

class Tokens:
    def __init__(self, tipoSimbolo, id, value=""):
        self.tipoSimbolo = tipoSimbolo
        self.value = value
        self.id = id #linea de codigo

    def prettyPrint(self):
        # simb = Symbols.Symbol()
        prettyPrint = "• Tipo Símbolo: " + str(self.tipoSimbolo) + ", línea: " + str(self.id) 
        if(self.value != ""):
            prettyPrint += ", Atributo: " + self.value + " "
        else:
            prettyPrint += " -"
        return prettyPrint