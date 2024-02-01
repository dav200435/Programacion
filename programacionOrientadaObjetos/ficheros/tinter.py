from tkinter import *
# Hold onto a global reference for the root window
root = None

def buttonPushed():
   file=open("fichero.txt","r")
   texto=file.read()
   txt.insert (END, str(texto))
   file.close()
   
def rellenar(texto):
  fichero=open("fichero.txt","w")
  fichero.write(texto)
  fichero.close()

def main():
  global root
  global txt
  root = Tk() 
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
  root.mainloop()

main()