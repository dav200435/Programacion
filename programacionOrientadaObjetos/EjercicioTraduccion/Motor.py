from tkinter import *
from Rueda import Rueda

class Motor:
    
    def __init__(self, tipo, caballos):
        self.__tipo = tipo
        self.__caballos = caballos
        

    @classmethod
    def switch(self):
        if self.button.config('text')[-1] == 'ON':
            self.button.config(text="OFF")
            Rueda.detener()
            
        else:
            self.button.config(text="ON")
            Rueda.girar()
   
    @classmethod
    def inyectarCarburante(self):
        ws = Tk()
        ws.title("Encender motor")
        ws.geometry("200x100")

        self.button = Button(ws, text="OFF", width=10, command=self.switch)
        self.button.pack()
        ws.mainloop()
