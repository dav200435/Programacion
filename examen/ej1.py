class stock:
    def __init__(self):
        self.piezas=[]
        self.cargarPiezas()
    
    def cargarPiezas(self):
        with open("piezas.txt","r") as file:
            fichero=file.readlines()
            for i in range (1,len(fichero)-1,2):
                if len(self.piezas)<501:
                    precioStock=fichero[i+1].split(" ")
                    insert={"pieza":fichero[i],"stock":precioStock[0],"precio":precioStock[1]}
                    self.piezas.append(insert)
                    
    def escribirFichero(self):
        with open("piezas.txt","w+") as file:
            file.write("")
        with open("piezas.txt","w") as file:
            file.write(f"{len(self.piezas)}\n")
            for i in self.piezas:
                file.write(f"{i['pieza']}{i['stock']} {i['precio']}")
                
    def anadirPieza(self):
        if len(self.piezas)>=500:
            print("Limite de piezas alcanzado")
            
        else:
            anadir=self.pedirDatos()
            with open("piezas.txt","w+") as file:
                self.piezas.append({"pieza":anadir[0],"stock":anadir[1],"precio":anadir[2]})
                self.escribirFichero()
        
    def pedirDatos(self):
        pieza=input("Nombre de la pieza-> ")+"\n"
        precio=input("Precio de la pieza-> ")+"\n"
        stock=input("stock de la pieza-> ")
        return pieza,stock,precio
    
    def runMenu(self):
        salir=True
        while salir:
            print("_"*16)
            print("1. Ver elementos")
            print("2. Guardar el fichero")
            print("3. añadir nueva pieza")
            print("4. Salir")
            print("_"*16)
            opcion=input("¿Que desea hacer? ")
            match opcion:
                case "1":
                    for i in range (len(self.piezas)):
                        print(self.piezas[i])
                case "2":
                    self.escribirFichero()
                case "3":
                    self.anadirPieza()
                case "4":
                    salir=False
                case _:
                    print("Opcion no soportada")
            
        print("¡Hasta la proxima!")

f=stock()
f.runMenu()