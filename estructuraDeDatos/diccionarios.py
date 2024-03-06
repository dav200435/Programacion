'''
biblioteca={
    "titulo":"mein Kampf",
    "isbn":"1234567890saf175sd75",
    "autor":"AdolfHitler",
    "edicion":3
}
biblioteca.update(isbn="12f3asf6a4sf31as6f5sa4f3")
print(biblioteca.get("titulo"))
print(biblioteca["titulo"])
print(biblioteca["isbn"])
'''

array = [12, 23, 5, 12, 5, 12, 5, 29, 92, 64, 23]
diccionario = {}
array2=[]

for i in range(len(array)):
    if array[i] in diccionario.keys():
        valor = diccionario[array[i]] + 1
        diccionario[array[i]] = valor
    else:
        diccionario[array[i]] = 1

print(diccionario)
for valor in diccionario.values():
    if valor not in array2:
        array2.append(valor)

print(array2)