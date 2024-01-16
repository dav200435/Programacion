import socket
from pynput import keyboard as kb

class cliente:
    def __init__(self):
        self.host=socket.gethostname()
        self.port=3000
        
        self.socketCliente=socket.socket()
        
    def conectar(self):
        self.socketCliente.connect((self.host,self.port))
        
    def detect_k(key):
        return key
        
    def correr(self):
        self.conectar()
        mensaje
        kb.Listener(self.detect_k).run
        while mensaje.lower()!="adios":
            if self.detect_k(kb)=="t":
                mensaje = input("-> ")
            self.socketCliente.send(mensaje.encode())
            datos=self.socketCliente.recv(1024).decode()
            print(f"Mensaje del server: {datos}")
            if mensaje == "exit":
                break
        self.socketCliente.close()

client=cliente()
client.correr()