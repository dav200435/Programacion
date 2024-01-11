class Libro:

    def __init__(self,titulo,autor,Publicacion):
        self.titulo=titulo
        self.autor=autor
        self.publicacion=Publicacion

    def __eq__(self,libro2):
        return self.titulo == libro2.titulo

    def __lt__(self,libro2):
        return self.titulo < libro2.titulo

libro2 = Libro("Don quijote","miguel de cervanes","1877")
libro1 = Libro("Geronimo Stilton","No l ose","2007")
libro4 = Libro("Don quijote","miguel de cervanes","1877")
libro3 = Libro("Geronimo Stilton","No l ose","2007")

if libro1 < libro2:
    print(libro1.titulo+" "+libro2.titulo)
else:
    print(libro4.titulo+" "+libro3.titulo)

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Baraja:
    def __init__(self):
        self.cartas = []
        palos = ['Oros', 'Vastos', 'Espadas', 'Copas']
        valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Sota", "Caballo", "Rey"]

        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(valor, palo))

    def __str__(self):
        return ", ".join(map(str, self.cartas))

    def __len__(self):
        return len(self.cartas)
    
miBaraja=Baraja()
print(miBaraja)
print(f"Tengo {len(miBaraja)} cartas en la baraja")
print()
for carta in range(len(miBaraja)):
    carta = miBaraja.cartas[carta]
    print(carta)