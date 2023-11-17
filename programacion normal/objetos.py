import random
class coche:
#definir la clase y darle caracteriaticas basicas
    def __init__(self,color,forma,ventanas,ruedas):
        self.color = color
        self.forma = forma
        self.ventanas = ventanas
        self.ruedes = ruedas
#instanciar la clase
f1=coche("verde","monoplaza","halo","lisas")
utilitario=coche("negro","monovolumen","normales","rugosas")

print(f1.color) 
class formula1:
    def __init__(self,Velocidad_Max,Piloto,escuderia):
        self.Velocidad_Max = Velocidad_Max
        self.piloto = Piloto
        self.escuderia = escuderia
nano=formula1("337","Fernando Alonso","Aston Martin")
print((nano.Velocidad_Max)+" "+(nano.piloto)+" "+(nano.escuderia))

class Perro:
    def __init__(self, nombre, raza, altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura

    def ladrar(self):
        ladridos = ["guau", "aaaauuuuuuuu", "gggrrrrrr"]
        random_ladrido = random.choice(ladridos)
        return random_ladrido

setter = Perro("Bolt", "De Agua", 0.5)
ladrido = setter.ladrar()
print(f"{setter.nombre} {setter.raza} {ladrido}")

class moto:
    def __init__(self,ruedas,sidecar,velocidad_max,plazas,aceleracion,velocidad):
        
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.sidecar = bool(sidecar)
        self.plazas = plazas
        self.aceleracion = aceleracion
        self.velocidad_max = velocidad_max
        
    def acelerar(self):
        self.velocidad = float(self.aceleracion)*1.5
        sonidos = ("watatatata","bbbrrrrr","ffffiiiiiuuuuuummmm")
        sonido_random = random.choice(sonidos)
        print(sonido_random)
        print(self.velocidad)
        self.velocidad = self.velocidad + self.aceleracion
    
    def velocimetro(self):
        print(f"la velocidad es {self.velocidad}")
        
ducatti = moto(2,False,350,1,6,0)
if __name__ == '__main__' :
    ducatti.velocimetro()
    ducatti.acelerar()
    ducatti.acelerar()
    ducatti.acelerar()
    ducatti.acelerar()
    ducatti.velocimetro()