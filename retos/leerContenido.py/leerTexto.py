fichero = open("imagen.jpg","r+b")


#with open(r+"fichero.txt") as file:
#    texto=file.readlines()
for i in fichero.read():
    print(i)
fichero.close()