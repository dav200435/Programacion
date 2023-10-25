class calculadora:
    def __init__(self,expresion):
        self.expresion = expresion
    
    def calcular(self):
        self.numa = ""
        self.operador = ""
        self.numb = ""
        estoyEnELOperador1 = True
        for caracter in self.expresion:
            if (caracter == "+" or caracter == "-" or caracter == "*" or caracter == "/" ):
                self.operador = caracter
                estoyEnELOperador1 = False
            else: 
                if estoyEnELOperador1 == True:
                    self.numa = self.numa + caracter
                else:
                    self.numb = self.numb + caracter    

        if (self.operador == "+"):
            self.sumar(self.numa,self.numb)
       
        if (self.operador == "-"):
            self.restar(self.numa,self.numb)
        
        if (self.operador == "*"):
            self.multiplicar(self.numa,self.numb)
        
        if (self.operador == "/"):
            self.dividir(self.numa,self.numb)
    
    def sumar(self,x,y):
        self.resultado=int(x)+int(y)
        print(self.resultado)
        
    def restar(self,x,y):
        self.resultado=int(x)-int(y)
        print(self.resultado)
   
    def multiplicar(self,x,y):
        self.resultado=int(x)*int(y)
        print(self.resultado)
        
    def dividir(self,x,y):
        self.resultado=int(x)/int(y)
        print(self.resultado)
        

print (calculadora (input()).calcular())
