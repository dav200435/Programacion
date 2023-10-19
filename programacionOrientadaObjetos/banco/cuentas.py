class CuaentaBancaria:
    def __init__(self,titular,saldo=0):
        
        self.titular=titular
        self.saldo=saldo
    def depositar(self):
        cantidad = input("Cuanto quieres depositar ")
        self.saldo + int(cantidad)
    def retirar(self):
        cantidad = input("cuanto desea retirar ")
        if (self.saldo < int(cantidad)):
            print("Saldo insuficiente")
        else: 
            self.saldo = self.saldo - int(cantidad)
            print(f"El nuevo saldo es de {self.saldo}")

                