import MySQLdb
import sys

class Db:
    def __init__(self):
        self.ip='127.0.0.1'
        self.name='Temperatura'
        self.user="root"
        self.passwd=""
        self.database=self.connect()
        
        
    def connect(self):
        try:
            self.DB=MySQLdb.connect(self.ip,self.user,self.passwd,self.name)
            print(f"connecting to {self.name}")
        except MySQLdb.Error as e:
            print(e)
            sys.exit()
    
    def insert(self,humedad,temp):
        cursor=self.DB.cursor()
        sql = f"insert into tamperaturas (humedad , temperatura) values ('{humedad}', '{temp}')"
        try:
            cursor.execute(sql)
            self.DB.commit()
            print("datos insertados")
        except MySQLdb.Error as e:
            print(e)
        finally:
            cursor.close()
            
            
    def getContent(self):
        cursor = self.DB.cursor()
        sql=f"select * from tamperaturas"
        try:
            cursor.execute(sql)
            registros=cursor.fetchall()
            records=[]
            for row in registros:
                records.append(f"{row[0]} | {row[1]} | {row [2]}")
            return records
        except MySQLdb.Error as e:
            return e
        finally:
            cursor.close()