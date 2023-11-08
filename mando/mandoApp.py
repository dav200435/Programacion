from tkinter import *
from mando import *

def Use():
    controller = controler("192.168.1.33")
    controller.Power()


root = Tk()
w = Label(root, text="mando a distancia")
w.pack()
powerBut = Button(root, text="Power", command = Use)
powerBut.pack()
exit=Button(root,text="Salir",command=root.destroy)
exit.pack()
root.mainloop()