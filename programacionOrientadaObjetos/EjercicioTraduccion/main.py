from Motor import Motor
from Rueda import Rueda
from Coche import Coche

ruedas1 = Rueda(20,"Pirelli")
ruedas2 = Rueda(20,"Pirelli")
ruedas3 = Rueda(20,"Pirelli")
ruedas4 = Rueda(20,"Pirelli")
ruedas = [ruedas1,ruedas2,ruedas3,ruedas4]

miCoche = Coche("Verde",80,3.2,Motor("Gasolina",170),ruedas)

miCoche.avanzar()
