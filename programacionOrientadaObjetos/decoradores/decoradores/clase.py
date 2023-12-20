class Persona:
    def __init__(self,nombre="",edad=0,dni=0):
       self.__nombre = nombre
       self.__edad = edad
       self.__dni = dni
       
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,value):
        self.__nombre=value
   
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,value):
        if self.comprobar(value):
            self.__edad=value
            
            
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,value):
        if self.comprobarDni(value):
            self.__dni=value
        else:
            print("Dni invalido")
    
    def comprobarDni(self,value):
        lista=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        if len(value) == 9:
            resto=int(value[:8])%23
            if value[8] == lista[resto]:
                return True
        raise ValueError("Dni invalido")
        
        
    def __str__(self):
        return self.__nombre + " " + str(self.__edad) + " " + str(self.__dni)

    def comprobar(self, value):
        if value>=18:
            return True
        return False
    
    
persona1=Persona()
try:
    persona1.dni="12345678J"
except ValueError as e:
    print(e)
persona1.dni = "51817498Q"
persona1.edad=19
persona1.nombre="Dario"
print(persona1)