import pyautogui
from cliente import *
import webbrowser


class Client(Cliente):
    def __init__(self):
        super().__init__()
        
    def enlace(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #abrir enlace de youtube
        
    def run(self):
        self.socketCliente.connect((self.host, self.port))
        while True:
            self.socketCliente.send(str(pyautogui.position()).encode())
            try:
                datos = self.socketCliente.recv(1024).decode()
                print(f"Servidor: {datos}")
                if datos == "enlace":
                    self.enlace()
            except:
                pass
            
        
         
if __name__ == "__main__":
    cli = Client()
    cli.run()