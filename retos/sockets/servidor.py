import socket

class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 3000
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.con, self.address = self.server_socket.accept()

    def detect_k(self, key):
        return key

    def correr(self):
        mensaje = ""

        while True:
            datos = self.con.recv(1024).decode()
            print(f"Enviado desde cliente: {datos}")
            mensaje = input("-> ")
            self.con.send(mensaje.encode())
            
            if datos.lower() == "exit":
                break

        self.con.close()