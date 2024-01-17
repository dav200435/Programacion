class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        print("Haciendo sonido")
        
class Perro(Animal):
    def __init__(self, nombre,raza,colorPelo):
        super().__init__(nombre)
        self.raza = raza
        self.pelo = colorPelo
    def hacer_sonido(self):
        print("Guau Guau")
mi_perro = Perro("Mario","Buldog Frances","Amarillo chillon")
print(mi_perro.pelo)


class AnimalMal:
    def __init__(self,nombre) #faltan los :
        self.nombre = nombre
    def hacer_sonido(self):
        print("Haciendo sonido")
        
class PerroMal(AnimalMal):
    def __init__(self, nombre,raza):
        super().__init__(nombre)
        self.raza = raza
    def hacer_sonido(self):
        print("Guau Guau")
mi_perro_Pocho = PerroMal("David","Yorkshire")
print(mi_perro.color_pelo) #No existe 