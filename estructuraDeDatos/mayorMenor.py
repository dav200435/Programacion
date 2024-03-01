lista=[1,45,6,123,3,-7]
def mayorMenor():
    mayor=lista[0]
    menor=lista[0]
    for i in lista:
        if i>mayor:
            mayor = i
        if i<menor:
            menor = i
    return f"El mayor es {mayor} y el menor es {menor}"

print(mayorMenor())