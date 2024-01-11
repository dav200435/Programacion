class pez:
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
    
    def __str__(self):
        return self.nombre+" "+self.raza
    
    def __eq__(self,item):
        return self.raza == item.raza

payaso = pez("nemo","Pez payaso")
atun = pez("Pescanova","atun")
payaso2 = pez("Papa de nemo","Pez payaso")
if payaso == payaso2:
    print("Estos peces son iguales")
else:
    print("Estos peces no tienen nada que ver")
if payaso == atun:
    print("Estos peces son iguales")
else:
    print("Estos peces no tienen nada que ver")