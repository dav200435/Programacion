class Empleados:
    def __init__(self, SalarioBase, bonos, nombre, apellido):
        self._salarioBase = SalarioBase
        self._bonos = bonos
        self._nombre=nombre
        self._apellido=apellido
    
    @property
    def correo(self):
        return self._nombre+self._apellido+"@dominio.extension"
        
    @property
    def salario(self):
        return  self._salarioBase + self._bonos
    
    @property
    def salarioBase(self):
        return self._salarioBase
    
    @salarioBase.setter
    def salarioBase(self,value):
        if value < 0:
            raise ValueError(f"{value} no es un valor correcto")
        self._salarioBase = value
    
    @property
    def bonos(self):
        return self._bonos
    
    @bonos.setter
    def bonos(self,value):
        if value<0:
            raise ValueError(f"{value} no es un valor correcto")
        self._bonos = value
                
Mario = Empleados(500,300,"mario","serradilla")
try:
    Mario.salarioBase = -50
except ValueError as e:
    print(e)
try:
    Mario.salarioBase = 550
except ValueError as e:
    print(e)

print(Mario.correo)
print(Mario.salario)