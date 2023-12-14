import math
class point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.x=0
        self.y=0
    def move(self,x,y):
        self.x=x
        self.y=y
        
    def distance(self,point):
        return math.sqrt((self.x-point.x)**2)+((self.y-point.y)**2)
        
            
        
coordenada1 = point(5,7)

coordenada2 = point(20,33)

print(coordenada1.distance(coordenada2))