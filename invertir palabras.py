palabra = input("Pon una palabra: ")
cadena_inv = ""
cont = len(palabra) 

while (cont > 0):
    cont = cont - 1
    cadena_inv = cadena_inv + palabra[cont]

print (cadena_inv)