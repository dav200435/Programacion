class point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value):
        self.__x = value
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,value):
        self.__y = value
    
    
class points:
    
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    
    def xGetter(self):
        return self.__x
    
    def yGetter(self):
        return self.__y
    
    def xSetter(self,value):
        self.__x=value
    
    def ySetter(self,value):
        self.__y=value