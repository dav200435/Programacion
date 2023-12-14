class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Error")
        self._celsius = valor
        
        



#uso
temp = Temperatura(15)
print(temp.celsius)
try:
    temp.celsius=-280
except ValueError:
    print("No puede ser menos a 0 Kelvin")
print(temp.celsius)
temp.celsius=35
print(temp.celsius)