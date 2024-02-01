# Import the required library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def buttonPushed():
   with open("fichero.txt", "r") as file:
        content = file.read()
        txt.insert(END, content)
   
def rellenar(texto):
  fichero=open("fichero.txt","w")
  fichero.write(texto)
  fichero.close()
# Create an instance of tkinter frame
def main():
    global root
    global txt
    root=Tk()
    # Set the geometry
    root.geometry("700x350")

    # Add a Scrollbar(horizontal)
    v=Scrollbar(root, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    w = Label(root, text="Vista de fichero") 
    w.pack()
    txt = Text(root, height = 5, width = 52)
    txt.pack()
    myButton = Button(root, text="Exit",command=buttonPushed)
    myButton.pack()
    escribir = Text(root, height = 5, width = 52)
    escribir.pack()
    boton = Button(root, text="Exit",command=rellenar(str(escribir.children)))
    boton.pack()
    # Add a text widget
    text=Text(root, font=("Georgia, 24"), yscrollcommand=v.set)
    # Attach the scrollbar with the text widget
    v.config(command=text.yview)
    text.pack()

    root.mainloop()

main()