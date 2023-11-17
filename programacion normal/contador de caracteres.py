cadena = input("")
vocales = 0
for i in cadena:
    if  i == "a" or i =="e" or i =="i" or i =="o" or i =="u":
        vocales += 1
print (cadena +" tiene "+ str(vocales)+" vocales")