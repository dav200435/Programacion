def tuplas():
    tupla1 = (1,2,3,4,5)
    tupla2 = (6,7,8,9)
    tupla3= tupla1 + tupla2
    print(tupla3)
diccionario1 = {
    "marca" : "BMW",
    "modelo" : "Benz"
}
diccionario2 = {
    "marca" : "Seat",
    "modelo" : "Picasso"
}

concesionario = [diccionario1, diccionario2]

print (concesionario[0]["modelo"])
#for i in concesionario:
#    print (i["marca"])