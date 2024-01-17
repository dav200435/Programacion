from cuentaBancaria import cuentaBancaria

class King(cuentaBancaria):
    def __init__(self, titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad)
        self._bonificacion=bonificacion
        self._edad=edad
    
    @property
    def bonificaion(self):
        return self.__bonificacion
    
    @bonificaion.setter
    def bonificacion(self,actualizacion):
        self.bonificaion = actualizacion
    
    def __str__(self):
        return super().__str__() + " " + str(self._bonificacion) + " " + str(self._edad)
    
    def ingreso(self, cantidad):
        if self.titularValido() and cantidad>0:
            self._cantidad += (cantidad * (1+(self._bonificacion/100)))
    
    def retiro(self, cantidad):
        if cantidad>0 and cantidad<=self._cantidad:
            self._cantidad -= cantidad
            
            
    def titularValido(self):
        if self._edad <= 25 and self._edad >=18:
            return True
        return False


titular1 = King("hola",1,3,27)
print(titular1)
titular1.ingreso(15)
print(titular1)
titular1.titular = "adios"
print(titular1)
titular1.ingreso(15)
print(titular1)