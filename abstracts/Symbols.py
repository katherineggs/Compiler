class Symbol:

    def __init__(self, identificador, nommbre, regEx):
        self.identificador = identificador
        self.nommbre = nommbre
        self.regEx = regEx

    def prettyPrint(self):
        print("-- Tipo: " + self.identificador + ", Nombre: " + self.nommbre+" --")