import MySQLdb

class DBUtils:
    def __init__(self):
        self.user = "root"
        self.passwd = ""
        self.db = "samur"
        self.ip = "127.0.0.1"
        self.database = self.__connect()
        
    def __connect(self):
        try:
            conn = MySQLdb.connect(self.ip, self.user, self.passwd, self.db)
            print(f"Connecting to {self.db}")
            return conn
        except MySQLdb.Error as e:
            print(f"Error connecting to database: {e}")
            return None
        
    def insert(self, values):
        if self.database is None:
            print("No database connection.")
            return
        cursor = self.database.cursor()
        try:
            for value in values:
                sql = ("INSERT INTO intervenciones (anio, mes, horaSolicitud, horaIntervencion, cod, distrito, hospital) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                data = (
                    value.getAnio(),
                    value.getMes(),
                    value.getHoraSolicitud(),
                    value.getHoraIntervencion(),
                    value.getCod(),
                    value.getDistrito(),
                    value.getHospital()
                )
                cursor.execute(sql, data)
            self.database.commit()
            print(f" Datos insertados con exito en {self.db}.intervenciones")
        except MySQLdb.Error as e:
            self.database.rollback()
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()
            self.database.close()