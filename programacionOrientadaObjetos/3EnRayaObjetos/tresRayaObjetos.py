
class tresEnRaya:
    def __init__(self,juego):
        self.juego = juego
    def comprobarGanador(self):
        def ganadora(self):
            if (cuadricula[0] == "x" and cuadricula[1] == "x" and cuadricula[2] == "x") or (cuadricula[3] == "x" and cuadricula[4] == "x" and cuadricula[5] == "x") or (cuadricula[6] == "x" and cuadricula[7] == "x" and cuadricula[8] == "x") or (cuadricula[0] == "x" and cuadricula[4] == "x" and cuadricula[8] == "x") or (cuadricula[2] == "x" and cuadricula[4] == "x" and cuadricula[6] == "x") or (cuadricula[0] == "x" and cuadricula[3] == "x" and cuadricula[6] == "x") or (cuadricula[1] == "x" and cuadricula[4] == "x" and cuadricula[7] == "x") or (cuadricula[1] == "x" and cuadricula[4] == "x" and cuadricula[7] == "x"):
                print("Gana jugador 1!!!")
                visualizar()
                print("Gana jugador 1!!!")
                return True
            return False

        def ganadorb():
            if (cuadricula[0] == "o" and cuadricula[1] == "o" and cuadricula[2] == "o") or (cuadricula[3] == "o" and cuadricula[4] == "o" and cuadricula[5] == "o") or (cuadricula[6] == "o" and cuadricula[7] == "o" and cuadricula[8] == "o") or (cuadricula[0] == "o" and cuadricula[4] == "o" and cuadricula[8] == "o") or (cuadricula[2] == "o" and cuadricula[4] == "o" and cuadricula[6] == "o") or (cuadricula[0] == "o" and cuadricula[3] == "o" and cuadricula[6] == "o") or (cuadricula[1] == "o" and cuadricula[4] == "o" and cuadricula[7] == "o") or (cuadricula[1] == "o" and cuadricula[4] == "o" and cuadricula[7] == "o"):
                print("Gana jugador 2!!!")
                visualizar()
                print("Gana jugador 2!!!")
                return True
            return False

class tablero:
    def __init__(self,casilla):
        self.casilla = casilla
        
    def comprobarCasilla(self):
        if (self.tablero[self.posicion-1] != " "):
            return False
        return True
    def anadirFicha(self):
        self.tablero[self.posicion-1] = self.valor