import tkinter as tk
from tkinter import ttk

# create a tkinter window
window = tk.Tk()
window.geometry("720x250")
window.title("Adding a Vertical Scrollbar to a Treeview Widget")

# create a treeview
tree = ttk.Treeview(window, columns=('Name', 'Age'))

# define the columns
tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

# add some data to the treeview
tree.insert('', 'end', '1', text='1', values=('Ram', 25))
tree.insert('', 'end', '2', text='2', values=('Mohan', 30))
tree.insert('', 'end', '3', text='3', values=('Shayam', 35))

# pack the treeview
tree.pack()

# start the main loop
window.mainloop()