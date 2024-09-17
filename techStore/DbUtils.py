import MySQLdb
 
class TechStore:
    def __init__(self):
        pass
 
    def conexion(self, usuario, contraseña):
        try:
            self.mibbdd = MySQLdb.connect("127.0.0.1", usuario, contraseña)
            print ("conectando...")
        except MySQLdb.Error as e:
            print (f"El error en conexion es: {e}")
 
    def crearBaseDatos (self):
        cursor = self.mibbdd.cursor()
        sql = "CREATE DATABASE TechStore;"
        try:
            cursor.execute(sql)
            print ("CREANDO BASE DE DATOS...")
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print (f"Error!!! {e}")
 
    def changeDataBase(self):
        cursor = self.mibbdd.cursor()
        sql = "USE TechStore;"
        try:
            cursor.execute(sql)
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print (f"Error usando la base de datos... {e}")
    def createTable (self):
        cursor = self.mibbdd.cursor()
        sql = "create table productos(id int primary key, nombre varchar(100), categoria varchar(50), cantidad int, precio double);"
        try:
            cursor.execute(sql)
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print (f"Error insertando tabla... {e}")
   
    def insert(self, nombre, categoria, cantidad, precio):
        cursor = self.mibbdd.cursor()
        sql = f"insert into productos(nombre, categoria, cantidad, precio)\
                values('{nombre}', '{categoria}', {cantidad}, {precio})"
        try:
            cursor.execute(sql)
            print("INSERTANDO DATOS...")
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print (f"Error insertando datos... {e}")
            
    def update (self, tabla, columna, valor, condicion):
        cursor = self.mibbdd.cursor()
        sql = f"update {tabla} set {columna} = {valor} where id = {condicion}"
        try:
            cursor.execute(sql)
            cursor.commit()
            print("actualizado con exito")
        except MySQLdb.Error as e:
            print(e)
        finally:
            cursor.close()
            
    def menu(self):
        pass
 
 
if __name__ == "__main__":
    tech = TechStore()
    tech.conexion("root", "")
    #tech.crearBaseDatos()
    tech.changeDataBase()
    #tech.createTable()
    tech.insert("Ordenador", "Electronica", 1, 894.99)