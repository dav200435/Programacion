
import os
import socket

HOST = "localhost"
PORT =  9999

client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

file = open("./imagen.jpg", "rb")

file.size = os.path.getsize("./imagen.jpg")

client.send("copied imagen.jpg".encode())
client.send(str(file.size).encode ())

data = file.read()

client.sendall (data)

client.send(b"<END>")

file.close()

client.close()
