class Rueda:
    
    def __init__(self,diametro,fabricante):
        self.__diametro=diametro
        self.__fabricante=fabricante

    @classmethod
    def girar(self):
        print("Las ruedas giran")
    
    @classmethod
    def detener(self):
        print("Se detiene el vehiculo")
