
fichero=open("fichero.txt","r")
def leer(f):
    lista=f.readlines()
    nombre=lista[0]
    tlfn=lista[1]
    nacimiento=lista[2]
    residencia=lista[3]
    chamba=lista[4]
    print(f"{nombre} con telefono {tlfn} necido en {nacimiento} vive en {residencia} y {chamba}")

leer(fichero)