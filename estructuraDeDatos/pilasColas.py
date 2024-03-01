'''
pila=[]
pila.append(2)
pila.append(5)
pila.append(2)
pila.append(8)
pila.append(0)
def intercambiador(new,old):
    for i in range (len(pila)):
        if pila[i] == old:
            pila[i] = new
    print(pila)

intercambiador(9,2)
'''
import random
import time
lista = []
for i in range (1,100000000):
    lista.append(i)
def buscar(num):
    cont=0
    stop=True
    while (cont < (len(lista)) and stop):
        if lista[cont]==num:
            stop=False
        cont+=1
    return f"El valor {num} esta en la posicion {cont}"

start_time = time.time()
print(buscar(99999099))
end_time = time.time()

# Calcular el tiempo transcurrido
tiempo_transcurrido = end_time - start_time
print(tiempo_transcurrido)