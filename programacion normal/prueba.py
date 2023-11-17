cadena = input("introduce un texto ")
cadena_inv = ""
for i in range (0,len(cadena)):
    # print (cadena[i])
    cadena_inv = cadena[i] + cadena_inv
print (cadena_inv)