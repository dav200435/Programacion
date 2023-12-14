class personaje:
    def __init__(self,vida,fuerza,defensa,nombre):
        self.vida=vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.nombre = nombre
    
    def atacar(self):
        pass

class mago(personaje):
    def __init__(self, vida, fuerza, defensa, nombre, magia):
        super().__init__(vida, fuerza, defensa, nombre)
        self.magia = magia

    def atacar(self):
        
        if self.magia>=4:
            print("Bola de fuego")
            self.magia = self.magia - 4
            return self.magia
        else:
            print("No te queda magia")
        
    def hablar(self):
        print("Hola que hay")

class guerrero(personaje):
    def __init__(self, vida, fuerza, defensa, nombre):
        super().__init__(vida, fuerza, defensa, nombre)
        self.defensa = defensa + 10
        self.vida = vida + 30

    def atacar(self):
        print("Da un espadazo")

    def hablar(self):
        print("Sabias que en terminos de")
        

class arquero(personaje):
    def __init__(self, vida, fuerza, defensa, nombre, flechas):
        super().__init__(vida, fuerza, defensa, nombre)
        self.flechas=flechas

    def atacar(self):
        if(self.flechas>0):
            print("Dispara una flecha")
            self.flechas-1
            return self.flechas
        else:
            print("necesitas mas flechas")
        
    def hablar(self):
        print("Hola que hay")