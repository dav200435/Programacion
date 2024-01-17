import pyautogui
from cliente import *

class Client(cliente):
    def __init__(self):
        super().__init__()
        
    def run(self):
        self.socketCliente.connect((self.host,self.port))
        while True:
            mensaje = str(pyautogui.position())
            self.socketCliente.send(mensaje.encode())
            

cli = Client()
cli.run()