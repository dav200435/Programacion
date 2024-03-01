import random
import time

array = []
for i in range (1,100000000):
    array.append(i)

def busqueda(num):
    array.sort()
    encontrado=True
    minimo = 0
    maximo = len(array) - 1
    
    while encontrado:
        mid = (minimo + maximo) // 2
        if array[mid] == num:
            encontrado=False
            return mid
        elif array[mid] < num and minimo!=maximo:
            minimo = mid + 1
        elif array[mid] > num and minimo!=maximo:
            maximo = mid - 1
        else:
            encontrado=False
            return "El numero especificado no aparece en la lista"
            

start_time = time.time()
print(busqueda(99999099))
end_time = time.time()

# Calcular el tiempo transcurrido
tiempo_transcurrido = end_time - start_time
print(tiempo_transcurrido)
