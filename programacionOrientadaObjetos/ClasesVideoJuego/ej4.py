class Edificio:
    def __init__(self, tipo, capacidad, coste):
        self.tipo = tipo
        self.capacidad = capacidad
        self.coste = coste
        self.construido = False

    def construir(self):
        self.construido = True
        print(f"{self.tipo} construido con capacidad de {self.capacidad} personas y cuesta {self.coste}.")

class Casa(Edificio):
    def __init__(self):
        super().__init__(tipo="Casa", capacidad=5, coste=160)

    def expandir(self):
        self.capacidad += 5
        self.coste += 58
        print(f"{self.tipo} expandido la nueva capacidad es {self.capacidad} y cuesta {self.coste}.")

class Granja(Edificio):
    def __init__(self):
        super().__init__(tipo="Granja", capacidad=10, coste=120)

    def expandir(self):
        self.capacidad += 3
        self.coste += 35
        print(f"{self.tipo} expandido la nueva capacidad es {self.capacidad} y cuesta {self.coste}.")

class Barraca(Edificio):
    def __init__(self):
        super().__init__(tipo="Barraca", capacidad=8, coste=80)

    def expandir(self):
        self.capacidad += 1
        self.coste += 12
        print(f"{self.tipo} expandido la nueva capacidad es {self.capacidad} y cuesta {self.coste}.")