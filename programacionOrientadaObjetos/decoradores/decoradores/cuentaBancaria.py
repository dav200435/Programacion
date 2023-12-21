class cuentaBancaria:
    def __init__(self,titular=None,cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad


    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,nombre):
        self.__titular = nombre
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return str(self.__titular) + " " + str(self.__cantidad)
    
    def ingreso(self,cantidad):
        if self.__titular != None and cantidad>0:
            self.__cantidad += cantidad
    
    
    def retiro(self,cantidad):
        if self.__titular != None and cantidad>0 and cantidad<=self.cantidad:
            self.__cantidad -= cantidad



titular1 = cuentaBancaria()
print(titular1)
titular1.ingreso(15)
print(titular1)
titular1.titular = "hola"
print(titular1)
titular1.ingreso(15)
print(titular1)