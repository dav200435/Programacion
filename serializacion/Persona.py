import json
class Person:
    def __init__(self,name,age,nickname):
        self.name=name
        self.age=age
        self.nickname=nickname
        
    def to_dict(self):
        data={}
        data['name']=self.name
        data['age']=self.age
        data['nickname']=self.nickname
        return data

A=Person("Persona1","34","Persona1")
B=Person("Persona2","51","Persona2")
peeps=[]
peeps.append(A.to_dict())
peeps.append(B.to_dict())

with open ("data.json","w") as file:
    json.dump(peeps,file)