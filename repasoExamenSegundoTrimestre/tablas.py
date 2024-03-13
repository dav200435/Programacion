import random
import tkinter as tk
import tkinter.messagebox as messagebox
import os

def tabla_n():
    number = random.randint(1, 10)
    print(number)
    with open("numero.txt", "w") as f:
        f.write("Tabla del: "+str(number) + "\n")
        for i in range(0, 11):
            numero = i * number
            f.write(f"{number} * {i} = {numero} \n")

def leerTabla_n():
    if os.path.exists("numero.txt"):
        with open("numero.txt", "r") as f:
            contenido = f.read()
            return contenido
    else:
        messagebox.showerror("Error 0x80072f8f - 0x20000", "Utilice el codigo de error 0x80072f8f - 0x20000 \npara ponerse en contacto con nuestro servicio. \nSentimos las molestias")

def mostrar_contenido(texto_widget):
    contenido = leerTabla_n()
    texto_widget.delete("1.0", tk.END) 
    texto_widget.insert(tk.END, contenido)

root = tk.Tk()
root.title("Contenido de numero.txt")

texto = tk.Text(root, wrap="word", height=15, width=50)
texto.pack(padx=10, pady=10)

boton_mostrar = tk.Button(root, text="Mostrar Contenido", command=lambda: mostrar_contenido(texto))
boton_mostrar.pack(pady=5)

boton_cambiar = tk.Button(root, text="Cambiar Contenido", command=tabla_n)
boton_cambiar.pack(pady=5)

boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
boton_cerrar.pack(pady=5)

root.mainloop()
