from Motor import Motor

class Coche:
    def __init__(self,color,velocidad,volumen,motor,ruedas):
        self.__color=color
        self.__velocidad=velocidad
        self.__volumen=volumen
        self.__ruedas=ruedas
        self.__motor=motor
    
    def avanzar(self):
        Motor.inyectarCarburante()
