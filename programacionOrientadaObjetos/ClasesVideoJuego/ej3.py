from abc import ABC, abstractmethod

class Habilidad(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

class AtaqueFisico(Habilidad):
    def ejecutar(self):
        print("ataca.")

class AtaqueMagico(Habilidad):
    def ejecutar(self):
        print("Bola de fuego")

class Curar(Habilidad):
    def ejecutar(self):
        print("HEAL")

class Personaje:
    def __init__(self, nombre, habilidades):
        self.nombre = nombre
        self.habilidades = habilidades

    def usar_habilidad(self, habilidad):
        print(f"{self.nombre} está utilizando la habilidad:")
        habilidad.ejecutar()