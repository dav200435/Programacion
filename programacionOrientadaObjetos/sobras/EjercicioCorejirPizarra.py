class Miclase:
    def __init__(self,nombre,e):
        self.nombre = nombre
        self.edad = e
    def saludar (self):
        print(f"Hola {self.nombre}")
#instancia = Miclase("David",25)
#resultado = 10/0
#instancia += "años"
#instancia.despedirse()
#print(instancia.apellido)

class Miclasecorrejida:
    def __init__(self,nombre,e,apellido):
        self.nombre = nombre
        self.edad = e
        self.apellido=apellido
    def saludar (self):
        print(f"Hola {self.nombre}")
    def despedirse(self):
        print(f"Adios {self.nombre},{self.apellido}")
instancia1 = Miclasecorrejida("David",25,"Serradilla")
try:
    resultado = 10/0
except ZeroDivisionError as e:
    print(f"{e}")
instancia1.nombre += "años"
instancia1.despedirse()
print(instancia1.apellido)
