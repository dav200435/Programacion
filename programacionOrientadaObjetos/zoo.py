from animal import Animal
class zoologico:
    def __init__(self,animales = []):
        self.animales = animales
        
    def addanimal(self,animal):
        self.animales.append (animal)
    
    def mostrar(self):
        for i in self.animales:
            print(f"Nombre: {i.nombre} Especie: {i.especie} Alimentacion: {i.alimentacion}")
            
zoo = zoologico()

zoo.addanimal(Animal("pepe","burro","zanahoria"))
zoo.mostrar()