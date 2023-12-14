from abc import ABC, abstractmethod

class Unidad(ABC):
    def __init__(self, nombre, rango_movimiento, poder_ataque):
        self.nombre = nombre
        self.rango_movimiento = rango_movimiento
        self.poder_ataque = poder_ataque

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def atacar(self):
        pass

class Infanteria(Unidad):
    def __init__(self, nombre, rango_movimiento, poder_ataque, blindaje):
        super().__init__(nombre, rango_movimiento, poder_ataque)
        self.blindaje = blindaje

    def mover(self):
        print(f"Infantería {self.nombre} se mueve {self.rango_movimiento} unidades.")

    def atacar(self):
        print(f"Infantería {self.nombre} ataca con un poder de {self.poder_ataque}.")

class Caballeria(Unidad):
    def __init__(self, nombre, rango_movimiento, poder_ataque, velocidad):
        super().__init__(nombre, rango_movimiento, poder_ataque)
        self.velocidad = velocidad

    def mover(self):
        print(f"Caballería {self.nombre} se mueve a una velocidad de {self.velocidad} unidades.")

    def atacar(self):
        print(f"Caballería {self.nombre} ataca con un poder de {self.poder_ataque}.")

class Arquero(Unidad):
    def __init__(self, nombre, rango_movimiento, poder_ataque, alcance):
        super().__init__(nombre, rango_movimiento, poder_ataque)
        self.alcance = alcance

    def mover(self):
        print(f"Arquero {self.nombre} se mueve {self.rango_movimiento} unidades.")

    def atacar(self):
        print(f"Arquero {self.nombre} ataca a distancia con un alcance de {self.alcance} unidades.")