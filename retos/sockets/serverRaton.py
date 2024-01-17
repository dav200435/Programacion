import socket
from server import *

class servidore(server):
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            datos = self.con.recv(1024).decode()
            print("Enviado desde cliente: " + str(datos))



mio = servidore()
mio.run()