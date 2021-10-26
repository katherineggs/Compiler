# Accepting de los DFAs
import scanner.DFAs as dfa

class Accepting:    
    def accepting(self, tipoDFA, palabra):
        if tipoDFA == 'id':
            movimientos = dfa.DFAs.DFAid
            if palabra[0].isdigit():
                inicio = "B"
            else:
                inicio = "A"
            accept = {"A", "B", "C"}
        elif tipoDFA=='int':
            movimientos = dfa.DFAs.DFAint
            inicio = "A"
            accept = {"A", "B", "C", "D", "E", "F"}

        estado = inicio
        for caracter in palabra:
            try:
                estado = movimientos[estado][caracter]
            except Exception:
                return False

            else:
                pass
        return estado in accept