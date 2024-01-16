import socket
import keyboard as kb

class server:
    
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 3000
        self.server_socket=socket.socket()
    
        
        #especificamos ip y puerto
        self.server_socket.bind((self.host,self.port))
        
        #cuantos clientes espera como maximo
        self.server_socket.listen(5)
        
        self.con,self.adress =self.server_socket.accept()
        
         
    def correr(self):
        mensaje

        while True:
            datos=self.con.recv(1024).decode()
        
            if datos == "exit":
                break
        
            print(f"Enviado desde cliente: {datos}")
        
            if kb.is_pressed("t"):
                mensaje = input("-> ")
        
            self.con.send(datos.encode())
        
        self.con.close()
        
serv=server()
serv.correr()