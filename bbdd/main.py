import sys
import MySQLdb

class db:
    
    def __init__(self):
        self.db = "127.0.0.1"
        self.port = 3006
        
    def connectDB(self,user,passwd,db):
        try:
            self.mydb = MySQLdb.connect(self.db,user,passwd,db)
            print(f"Connecting to {db}")
        except MySQLdb.Error as e:
            print(e)
            sys.exit(1)
            
    def insertUsers(self, nombre, edad, apellidos):
        cursor = self.mydb.cursor()
        try:
            cursor.execute(f"SELECT * FROM usuarios WHERE nombre = '{nombre}'")
            existing_user = cursor.fetchone()
            if existing_user:
                print("El usuario ya existe en la base de datos.")
            else:
                sql = f"INSERT INTO usuarios (nombre, edad, apellidos) VALUES ('{nombre}', {int(edad)}, '{apellidos}')"
                cursor.execute(sql)
                self.mydb.commit()
                print("Usuario insertado correctamente.")
        except MySQLdb.Error as e:
            print(e)
        
    def consultausuarios(self):
        cursor = self.mydb.cursor()
        sql=f"select * from usuarios"
        try:
            cursor.execute(sql)
            print(str(cursor.rowcount))
            registros=cursor.fetchall()
            print("id | nombre | edad | apellido")
            for row in registros:
                print(f"{row[0]} | {row[1]} | {row [2]} | {row[3]}")
        except MySQLdb.Error as e:
            print(e)
        
    def buscarUser(self, nombre):
        try:
            cursor = self.mydb.cursor()
            sql =f"SELECT * FROM usuarios WHERE nombre = '{nombre}'"
            cursor.execute(sql)
            registros = cursor.fetchall()
            for row in registros:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        except MySQLdb.Error as e:
            print("Error executing MySQL query:", e)
            
            
    def UpdateName(self, user, newName):
        try:
            cursor = self.mydb.cursor()
            sql = f"UPDATE usuarios SET nombre = '{newName}' WHERE nombre = '{user}'"
            cursor.execute(sql)
            self.mydb.commit()
            print("Actualizado con exito")
        except MySQLdb.Error as e:
            print(e)
            
    
        
    
if __name__ == "__main__":
    mibase=db()
    mibase.connectDB("root","","dam")
    mibase.insertUsers("mario",20,"serradilla")
    mibase.insertUsers("daniel",19,"zapata")
    #mibase.consultausuarios()
    #mibase.buscarUser("daniel")