import MySQLdb
import sys
from tkinter import messagebox

class DBUtils:
    def __init__(self):
        self.user = "root"
        self.passwd = ""
        self.db = "agenda"
        self.ip = "127.0.0.1"
        self.database = self.__connect()

    def __connect(self):
        try:
            conn = MySQLdb.connect(self.ip, self.user, self.passwd, self.db)
            print(f"Connecting to {self.db}")
            return conn
        except MySQLdb.Error as e:
            return e
        
    def confirmLogin(self, username):
        cursor = self.database.cursor()
        try:
            sql = f"SELECT * FROM usuarios WHERE Usuario = '{username}'"
            cursor.execute(sql)
            user = cursor.fetchone()
            if user:
                return user
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
        
    def returnNotes(self,user):
        cursor = self.database.cursor()
        sql=f"select * from notas where User = {user.id}"
        try:
            cursor.execute(sql)
            registros=cursor.fetchall()
            records=[]
            for row in registros:
                records.append(f"{row[0]} | {user.user} | {row [2]} | {row[3]}")
            return records
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
            
    def findNote(self,text,user):
        cursor = self.database.cursor()
        sql=f"select * from notas where note like '{text}' and User = {user.id}"
        try:
            cursor.execute(sql)
            registros=cursor.fetchall()
            records=[]
            for row in registros:
                records.append(f"{row[0]} | {user.user} | {row [2]} | {row[3]}")
            return records
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
            
    def createUser(self, nombre, apellido, user):
        cursor = self.database.cursor()
        try:
            cursor.execute(f"SELECT * FROM usuarios WHERE Usuario = '{user}'")
            existing_user = cursor.fetchone()
            if existing_user:
                return messagebox.showerror("Error", "Nombre de usuario en uso")
            else:
                sql = f"INSERT INTO usuarios (nombre, apellido, Usuario) VALUES ('{nombre}','{apellido}', '{user}')"
                cursor.execute(sql)
                self.database.commit()
                return messagebox.showinfo("Creado", "El usuario se creo con exito")
        except MySQLdb.Error as e:
            return messagebox.showerror('Error','e')
        finally:
            cursor.close()
    
    def deleteNote(self, note_id):
        cursor = self.database.cursor()
        try:
            sql = f"DELETE FROM notas WHERE id = {note_id}"
            cursor.execute(sql)
            self.mydb.commit()
            return messagebox.showinfo("Eliminado", "La nota se ha eliminado correctamente")
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()

    def deleteUser(self, user):
        cursor = self.database.cursor()
        try:
            sql = f"DELETE FROM usuarios WHERE id = {user.id}"
            cursor.execute(sql)
            self.mydb.commit()
            return messagebox.showinfo("Eliminado", "El usuario se ha eliminado correctamente")
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()
