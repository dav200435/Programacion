import turtle
turtle.color("green","blue")
turtle.end_fill()
class FormaGeometrica:
    def dibujar(self):
        pass

class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        for _ in range(4):
            turtle.forward(self.lado)
            turtle.right(90)

class Triangulo(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        for _ in range(3):
            turtle.forward(self.lado)
            turtle.right(120)

class Circulo (FormaGeometrica):
    def __init__(self,lado):
        self.lado = lado
    
    def dibujar(self):
        for i in range(365):
            turtle.forward(self.lado)
            turtle.right(1)
    
def dibujar_forma(forma):
    forma.dibujar()

cuadrado = Cuadrado(100)
triangulo = Triangulo(100)
circulo = Circulo(1)
dibujar_forma(cuadrado)
dibujar_forma(triangulo)
dibujar_forma(circulo)
turtle.done()