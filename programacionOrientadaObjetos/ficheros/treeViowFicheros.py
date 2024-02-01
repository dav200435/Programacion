import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime

# create a tkinter window
window = tk.Tk()
window.geometry("720x250")
window.title("Adding a Vertical Scrollbar to a Treeview Widget")

# create a treeview
tree = ttk.Treeview(window, columns=('elemento','modificado','ult_acceso','tamaño'))

# define the columns
tree.column('#0',width=0)
tree.heading('elemento', text='archivo')
tree.heading('modificado', text='Ultima modificacion')
tree.heading('ult_acceso', text='Ultimo acceso')
tree.heading('tamaño', text='Tamaño')

# add some data to the treeview

ruta_app = os.getcwd()  # obtiene ruta del script 
print (ruta_app)
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
linea = '-' * 40
contador=0
print (contenido)
for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    print (os.path.isfile(archivo))
    #if not os.access(archivo, os.R_OK) and os.path.isfile(archivo):
    estado = os.stat(archivo)  # obtiene estado del archivo
    tamaño = estado.st_size  # obtiene de estado el tamaño 
    
    # Obtiene del estado fechas de último acceso/modificación
    # Como los valores de las fechas-horas vienen expresados
    # en segundos se convierten a tipo datetime. 
    
    ult_acceso = datetime.fromtimestamp(estado.st_atime)
    modificado = datetime.fromtimestamp(estado.st_mtime)
    
    # Se aplica el formato establecido de fecha y hora
    
    ult_acceso = ult_acceso.strftime(formato)
    modificado = modificado.strftime(formato)
    
    # Se acumulan tamaños y se muestra info de cada archivo
    
    tree.insert('', 'end',text=(contador), values=(elemento,modificado,ult_acceso,round(tamaño/1024, 1)))
    contador+=1
# pack the treeview
tree.pack()

# start the main loop
window.mainloop()