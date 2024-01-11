class coche:
    def __init__(self,marca,modelo,potencia):
        self.marca=marca
        self.modelo=modelo
        self.potencia=potencia
    def __gt__(self,otro):
        return self.potencia>otro.potencia

coche1=coche("formula1","red bull",800)
coche2=coche("ciclomotor","Marca generica",20)
if coche1>coche2:
    print("Mi coche es mas potente")
else:
    print("Mi coche palma seguro")
if coche2>coche1:
    print("Mi coche es mas potente")
else:
    print("Mi coche palma seguro")