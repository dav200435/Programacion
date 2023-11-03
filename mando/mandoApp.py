from tkinter import *
from mando import *

def Use():
    minicontroller = controler("192.168.1.33")
        
root = Tk()
w = Label(root, text="mando a distancia")
w.pack()
powerBut = Button(root, text="power Switch", command = Use)
powerBut.pack()
root.mainloop()