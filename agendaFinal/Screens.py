import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from agenda.DBUtils import DBUtils
from agenda.User import User

class Application:
    def __init__(self):
        self.database = DBUtils()
        self.user = None
        self.root = tk.Tk()
    
    def printScreen(self):
        self.root.geometry('500x400')
        self.root.configure(bg='beige')
        self.root.title('aplicacion')
        self.tinfo = tk.Text(self.root, width=50, height=10)
        self.tinfo.pack(side='top')
        self.button = ttk.Button(self.root, text='Exit', command=quit)
        self.button.pack(side='bottom')
        self.button2 = ttk.Button(self.root, text='ver info', command=self.consulta)
        self.button2.pack(side='bottom')
        
        self.login_button = ttk.Button(self.root, text='Iniciar Sesión', command=self.loginScreen)
        self.login_button.pack(side='bottom')
        
        self.root.mainloop()
    
    def consulta(self):
        if self.user:    
            self.tinfo.delete('1.0', tk.END)
            consultas = self.database.returnNotes(self.user)
            for row in consultas:
                self.tinfo.insert(tk.END, row + '\n')
        else:
            self.tinfo.delete('1.0', tk.END)
            self.tinfo.insert(tk.END,'Inicia sesion para poder ver las notas')
            
    def loginScreen(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.geometry('300x150')
        self.login_window.title('Inicio de Sesión')
        
        self.label_username = ttk.Label(self.login_window, text='Usuario:')
        self.label_username.pack()
        self.entry_username = ttk.Entry(self.login_window)
        self.entry_username.pack()
        
        self.button_login = ttk.Button(self.login_window, text='Iniciar Sesión', command=self.validateLogIn)
        self.button_login.pack(side='top')

        self.button_register = ttk.Button(self.login_window, text='Registro', command=self.registerScreen)
        self.button_register.pack(side='bottom')
        self.register = ttk.Label(self.login_window, text='¿No tienes cuanta? registrate')
        self.register.pack(side='bottom')
        

    def validateLogIn(self):
        username = self.entry_username.get()
        user = self.database.confirmLogin(username)
        if user:
            self.user = User(user[3],user[0],user[1])
            messagebox.showinfo('Exito','Se ha iniciado sesión con exito')
        else:
            messagebox.showerror('Error', 'El usuario no existe')
            self.user=None

    def registerScreen(self):
        self.register_window = tk.Toplevel(self.root)
        self.register_window.geometry('300x150')
        self.register_window.title('Registro de Usuario')

        self.labelName = ttk.Label(self.register_window, text='nombre:')
        self.labelName.pack()
        self.entryName = ttk.Entry(self.register_window)
        self.entryName.pack()

        self.surname = ttk.Label(self.register_window, text='Apellido:')
        self.surname.pack()
        self.entrySurname = ttk.Entry(self.register_window)
        self.entrySurname.pack()
        
        self.labelUsername = ttk.Label(self.register_window, text='Usuario:')
        self.labelUsername.pack()
        self.entryUsername = ttk.Entry(self.register_window)
        self.entryUsername.pack()

        self.button_register_user = ttk.Button(self.register_window, text='Registrar', command=self.registerUser)
        self.button_register_user.pack(side='bottom')

    def registerUser(self):
        username = self.entryName.get()
        surname = self.entrySurname.get()
        user = self.entryUsername.get()
        if len(username)>0 and len(surname)>0 and len(user)>0 :
            self.database.createUser(username,surname,user)
        else:
            messagebox.showerror('Error','Uno de los campos no ha sido rellenado')
        
if __name__ == '__main__':
    app = Application()
    app.printScreen()