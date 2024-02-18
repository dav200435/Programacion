class figura:
    def __init__(self,vertices=3,relleno=True):
        self.vertices=vertices
        self.relleno=relleno
    
    def contarVertices(self):
        print(f"la figura teine {self.vertices} vertices")
    
    def relleno(self):
        if self.relleno:
            print("la figura ira rellena")

class cuadrado(figura):
    
    def __init__(self, lado, relleno=True):
        super().__init__(relleno)
        self.lado=lado
    
    def calcularArea(self):
        print(self.lado*self.lado)
    
    def relleno(self):
        if self.relleno:
            print("El cuadrado ira relleno")
            
class circulo(figura):
    
    def __init__(self, radio=1, relleno=True):
        super().__init__(relleno)
        self.radio=radio
    
    def calcularArea(self):
        print(3.14*(self.radio**2))
        
    def relleno(self):
        if self.relleno:
            print("El circulo ira relleno")
        
class triangulo(figura):
    def __init__(self, base, altura, relleno=True):
        super().__init__(relleno)
        self.alto=altura
        self.base=base
    
    def calcularArea(self):
        print((self.base*self.alto)/2)
        
    def relleno(self):
        if self.relleno:
            print("El triangulo ira relleno")