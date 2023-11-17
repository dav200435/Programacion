cadena = [2,3,3,2,2,2,4,5,6,3,2,7,2]
#while 2 in cadena:
#    cadena.remove(2)
for l in (0,len(cadena)):
    if cadena[l]=='2':
        cadena.remove(2)
print (cadena)