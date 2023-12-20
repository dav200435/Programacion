class ejemplo:
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self,valor):
        self.__altura=valor
    
    @altura.deleter
    def altura(self):
        del self.__altura
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,valor):
        self.__edad = valor
        
    @edad.deleter
    def edad(self):
        del self.__edad

e=ejemplo()
e.edad = 30
#e.__privateEdad()
print(e.edad)
del e.edad
print(e.edad)