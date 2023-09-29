import random
numero = 0
aleatorio = random.randint(1, 100)
while (numero != aleatorio):
  numero = input ("Estoy pensando en un número del 1 al 100 adivinalo ")
  numero = int(numero)
  if (numero > aleatorio):
    print ("pon un poquito menos que no te cuenta nada")
  else:
    print ("a donde vas ya te has pasado")


print ("Exacto es " + str(aleatorio))