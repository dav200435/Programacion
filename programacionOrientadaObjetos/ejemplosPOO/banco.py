from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre, apellidos, nif):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = nif

class Cuenta(ABC):
    def __init__(self, cliente, numerocuenta):
        self.cliente = cliente
        self.numerocuenta = numerocuenta
        self.saldo = 0
    
    def get_numerocuenta(self):
        print(self.numerocuenta)
    
    def get_saldo(self):
        print(self.saldo)
    
    def get_cliente(self):
        print(self.cliente)
    
    def ingresar(self, cantidad):
        self.saldo += cantidad
    
    @abstractmethod
    def retirar(self, cantidad):
        pass
    
    @abstractmethod
    def actualizarSaldo(self):
        pass

class CuentaCorriente(Cuenta):
    def __init__(self, cliente, numerocuenta):
        super().__init__(cliente, numerocuenta)
        self.interes = 1.5
    
    def __str__(self):
        return f"Cuenta Corriente - Cliente: {self.cliente.nombre} {self.cliente.apellidos}, Número de Cuenta: {self.numerocuenta}, Saldo: {self.saldo}"
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
    
    def actualizarSaldo(self):
        self.saldo += self.saldo * (self.interes / 100)

class CuentaAhorro(Cuenta):
    def __init__(self, cliente, numerocuenta, interes_variable, saldo_minimo):
        super().__init__(cliente, numerocuenta)
        self.interes_variable = interes_variable
        self.saldo_minimo = saldo_minimo
    
    def __str__(self):
        return f"Cuenta Ahorro - Cliente: {self.cliente.nombre} {self.cliente.apellidos}, Número de Cuenta: {self.numerocuenta}, Saldo: {self.saldo}"
    
    def retirar(self, cantidad):
        if self.saldo - cantidad >= self.saldo_minimo:
            self.saldo -= cantidad
    
    def actualizarSaldo(self):
        self.saldo += self.saldo * (self.interes_variable / 100)