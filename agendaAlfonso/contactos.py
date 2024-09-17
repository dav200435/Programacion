## CLASES DEL MODELO DE DATOS

class Contacto():
    
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getApellido(self):
        return self._apellido
    
    def setApellido(self, apellido):
        self._apellido = apellido
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
