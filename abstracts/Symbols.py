class Symbol:

    def __init__(self, identificador, regEx, nommbre):
        self.identificador = identificador
        self.nommbre = nommbre
        self.regEx = regEx

    def prettyPrint(self):
        print("-- Tipo: " + self.identificador + ", Nombre: " + self.nommbre+" --")

    def __str__(self):
        prettySimbolo = str(self.nommbre)
        return prettySimbolo