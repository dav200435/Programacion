'''
count=0
with open(r"ficheroDatos.txt") as fichero:
    for linea in fichero:
        print(linea)
        cadena=linea.split(";")
        print (cadena[count])
        count+=1
'''
class persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        
class listaPersonas:
    
    def __init__(self):
        self.listaPersonas=[]
    
    def computo(self,fichero):
        for linea in fichero:
            listaPalabras=linea.split(";")
            perso=persona(listaPalabras[0],listaPalabras[1],listaPalabras[2])
            self.listaPersonas.append(perso)
            
fichero = open("ficheroDatos.txt","r")
personas=listaPersonas()
personas.computo(fichero)
count=0
for i in personas.listaPersonas:
    print(personas.listaPersonas[count])
