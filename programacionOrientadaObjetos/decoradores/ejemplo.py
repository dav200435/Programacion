class ejemplo:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)
    
    
e=ejemplo("Dario","Arroyo",19)
print(e)