from abc import ABC, abstractmethod

class persona:
    def __init__(self,provincia):
        self.provincia=provincia
    
class legislador(persona,ABC):
    
    def __init__(self, provincia, sueldo=54000):
        super().__init__(provincia)
        self.sueldo=sueldo
    
    @abstractmethod
    def getcamara(self):
        pass
    
class Diputado(legislador):
    
    def __init__(self, provincia, nombre, sueldo=54000):
        super().__init__(provincia, sueldo)
        self.nombre=nombre
        
    def getcamara(self):
        print(f"El diputado {self.nombre} trabaja en {self.provincia}")
        
class Senador(legislador):
    def __init__(self, provincia, nombre, sueldo=54000):
        super().__init__(provincia, sueldo)
        self.nombre=nombre
    
    def getcamara(self):
        print(f"El senador {self.nombre} trabaja en {self.provincia}")
