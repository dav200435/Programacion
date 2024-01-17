import socket

class Cliente:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 3000
        self.socketCliente = socket.socket()

    def conectar(self):
        self.socketCliente.connect((self.host, self.port))

    def detect_k(self, key):
        return key

    def correr(self):
        self.conectar()
        mensaje = ""
        while mensaje.lower() != "exit":
            mensaje = input("-> ")
            self.socketCliente.send(mensaje.encode())
            datos = self.socketCliente.recv(1024).decode()
            print(f"Mensaje del servidor: {datos}")

            if mensaje.lower() == "exit":
                break

        self.socketCliente.close()

client = Cliente()
client.correr()