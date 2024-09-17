from Db import Db
from Arduino import Arduino

class Refactor:
    def __init__(self):
        self.arduino=Arduino()
        self.data=self.arduino.conect()
        self.db=Db()
    
    def refactorData(self):
        self.data = self.data.split()
        if self.data[1]!="nan" and self.data [3]!= "nan":
            self.db.insert(self.data[1],self.data[3])
        else:
            print("datos incorrectos")
            
    def printData(self):
        data=self.db.getContent()
        print("id | humedad | temperatura |")
        for row in data:
            print(row)