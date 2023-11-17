
class vehiculo:
    
    def __init__(self,marca,modelo,color,kilometraje):
        
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = kilometraje
        
    def conducir(self):
        kilometrosConducidos=input("cuantos kilometros has conducido ")
        self.kilometraje = self.kilometraje + int(kilometrosConducidos)
        print(f"has conducido {self.kilometraje} conducido")
            
audi = vehiculo("audi","a4","azul",123)
audi.conducir()