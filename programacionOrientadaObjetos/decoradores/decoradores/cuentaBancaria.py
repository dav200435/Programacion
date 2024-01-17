class cuentaBancaria:
    def __init__(self,titular=None,cantidad=0):
        self._titular = titular
        self._cantidad = cantidad


    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self,nombre):
        self._titular = nombre
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad

    def __str__(self):
        return str(self._titular) + " " + str(self._cantidad)
    
    def ingreso(self,cantidad):
        if self._titular != None and cantidad>0:
            self._cantidad += cantidad
    
    
    def retiro(self,cantidad):
        if self._titular != None and cantidad>0 and cantidad<=self.cantidad:
            self._cantidad -= cantidad



titular1 = cuentaBancaria()
print(titular1)
titular1.ingreso(15)
print(titular1)
titular1.titular = "hola"
print(titular1)
titular1.ingreso(15)
print(titular1)
