class listas:
    def __init__(self,array,value) -> None:
        self.array=array
        self.value=value
    
    def eliminarValor(self):
        eliminar=[]
        for i in range (len(self.array)):
            if self.array[i]==self.value:
                eliminar.append(i)
                
        eliminar.reverse()
        for  j in eliminar:
            self.array.pop(j)
        print(self.array)
        
    def lista2D(self):
        for i in range (len(self.array)):
            for j in range (len(self.array[i])):
                print(self.array[i][j])
    
    def lista3D(self):
        for i in range (len(self.array)):
            for j in range (len(self.array[i])):
                for z in range (len(self.array[i][j])):
                    print(self.array[i][j][z])
                    
        
        
array=[[[1,2,3],[1,2,3],[1,2,3]],[[4,5,6],[4,5,6],[4,5,6]],[[7,8,9],[7,8,9],[7,8,9]]]
buscador=listas(array,3)
buscador.lista3D()