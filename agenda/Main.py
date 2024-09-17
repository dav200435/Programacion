import tkinter as tk
from tkinter import ttk
import sys

from Screens import Screens

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla Principal")
        self.root.geometry("300x200")

        # Crear instancia de Screens
        self.screens = Screens()

        # Botones para acceder a diferentes pantallas
        login_button = ttk.Button(self.root, text="Iniciar Sesión", command=self.showLogInScreen)
        login_button.pack(pady=10)

        notes_button = ttk.Button(self.root, text="Ver Notas", command=self.showNotesScreen)
        notes_button.pack(pady=10)

        create_user_button = ttk.Button(self.root, text="Crear Usuario", command=self.createUserScreen)
        create_user_button.pack(pady=10)

        delete_note_button = ttk.Button(self.root, text="Eliminar Nota", command=self.deleteNoteScreen)
        delete_note_button.pack(pady=10)

        delete_user_button = ttk.Button(self.root, text="Eliminar Usuario", command=self.DeleteUserScreen)
        delete_user_button.pack(pady=10)

    def showLogInScreen(self):
        self.root.withdraw()
        self.screens.login_screen()

    def showNotesScreen(self):
        self.root.withdraw()
        user = {'id': 1, 'user': 'nombre_de_usuario'}
        self.screens.show_notes_screen(user)

    def createUserScreen(self):
        self.root.withdraw()
        self.screens.create_user_screen()

    def deleteNoteScreen(self):
        self.root.withdraw()
        self.screens.delete_note_screen()

    def DeleteUserScreen(self):
        self.root.withdraw()
        user = {'id': 1, 'user': 'nombre_de_usuario'}
        self.screens.delete_user_screen(user)



if __name__ == "__main__":
    root = tk.Tk()
    app = MainScreen(root)
    root.mainloop()
    sys.exit()
