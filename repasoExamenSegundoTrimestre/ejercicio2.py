array=[]
with open("index.txt","r")as file:
    fichero=file.readlines()
    for linea in fichero:
        array.append(linea)
print(array)
array.reverse()
print(array)