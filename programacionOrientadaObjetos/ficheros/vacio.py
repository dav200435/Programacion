import os

lista = os.listdir(path=".")
for i in range (len(lista)):
    print(lista[i])
    if lista[i] =="vacio.py":
        print("Encontrado")
        with open(lista[i]) as file:
            print(file.read())
        break
            