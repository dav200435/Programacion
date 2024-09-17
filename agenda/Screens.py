import tkinter as tk
from tkinter import ttk, messagebox
from DBUtils import DBUtils
from User import User

class Screens:
    def __init__(self):
        self.database = DBUtils()

    def login_screen(self):
        login_window = tk.Tk()
        login_window.title("Iniciar sesión")
        login_window.geometry("300x150")

        def handle_login():
            username = username_entry.get()

        username_label = ttk.Label(login_window, text="Usuario:")
        username_label.pack(pady=5)
        username_entry = ttk.Entry(login_window)
        username_entry.pack(pady=5)

        login_button = ttk.Button(login_window, text="Iniciar Sesión", command=handle_login)
        login_button.pack(pady=5)

        login_window.mainloop()

    def show_notes_screen(self, user):
        notes_window = tk.Tk()
        notes_window.title("Notas")
        notes_window.geometry("500x300")

        table = ttk.Treeview(notes_window)
        table['columns'] = ('ID', 'User', 'Titulo', 'Nota')

        table.column('#0', width=0, stretch=tk.NO)
        table.column('ID', anchor=tk.CENTER, width=100)
        table.column('User', anchor=tk.CENTER, width=100)
        table.column('Titulo', anchor=tk.CENTER, width=100)
        table.column('Nota', anchor=tk.CENTER, width=100)
        
        data = self.database.returnNotes(user)
        
        for idx, row in enumerate(data, start=1):
            table.insert(parent='', index='end', iid=idx, values=row)

        table.pack(padx=10, pady=10)

        notes_window.mainloop()

    def create_user_screen(self):
        create_user_window = tk.Tk()
        create_user_window.title("Crear Usuario")
        create_user_window.geometry("300x200")

        def create_user():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            username = username_entry.get()

        nombre_label = ttk.Label(create_user_window, text="Nombre:")
        nombre_label.pack(pady=5)
        nombre_entry = ttk.Entry(create_user_window)
        nombre_entry.pack(pady=5)

        apellido_label = ttk.Label(create_user_window, text="Apellido:")
        apellido_label.pack(pady=5)
        apellido_entry = ttk.Entry(create_user_window)
        apellido_entry.pack(pady=5)

        username_label = ttk.Label(create_user_window, text="Nombre de Usuario:")
        username_label.pack(pady=5)
        username_entry = ttk.Entry(create_user_window)
        username_entry.pack(pady=5)

        create_button = ttk.Button(create_user_window, text="Crear Usuario", command=create_user)
        create_button.pack(pady=5)

        create_user_window.mainloop()

    def delete_note_screen(self):
        delete_note_window = tk.Tk()
        delete_note_window.title("Eliminar Nota")
        delete_note_window.geometry("300x150")

        def delete_note():
            note_id = note_id_entry.get()
            
        note_id_label = ttk.Label(delete_note_window, text="ID de la Nota:")
        note_id_label.pack(pady=5)
        note_id_entry = ttk.Entry(delete_note_window)
        note_id_entry.pack(pady=5)

        delete_button = ttk.Button(delete_note_window, text="Eliminar Nota", command=delete_note)
        delete_button.pack(pady=5)

        delete_note_window.mainloop()

    def delete_user_screen(self):
        delete_user_window = tk.Tk()
        delete_user_window.title("Eliminar Usuario")
        delete_user_window.geometry("300x150")

        def delete_user():
            user_id = user_id_entry.get()
            
        user_id_label = ttk.Label(delete_user_window, text="ID del Usuario:")
        user_id_label.pack(pady=5)
        user_id_entry = ttk.Entry(delete_user_window)
        user_id_entry.pack(pady=5)

        delete_button = ttk.Button(delete_user_window, text="Eliminar Usuario", command=delete_user)
        delete_button.pack(pady=5)

        delete_user_window.mainloop()
