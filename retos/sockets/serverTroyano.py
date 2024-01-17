from servidor import *
from pynput.keyboard import Listener
import sys

class servidore(Server):
    def __init__(self):
        super().__init__()
    
    def captura(self,key):
        tecla=str(key)
        if tecla=="'t'":
                mensaje=input("-> ")
                self.con.send(mensaje.encode())
        with open("log.txt","a") as f:
            f.write(tecla)
        if tecla == "Key.esc":
            sys.exit()

    
    def run(self):
        with Listener (on_press=self.captura) as c:
            c.join()
            
                
            

if __name__ == "__main__":
    mio = servidore()
    mio.run()