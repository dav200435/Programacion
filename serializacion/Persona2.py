import json

class Person:
    def __init__(self, name, age, nickname):
        self.name = name
        self.age = age
        self.nickname = nickname
        
    def to_dict(self):
        data = {
            'name': self.name,
            'age': self.age,
            'nickname': self.nickname
        }
        return data

with open("data.json", "r") as file:
    data = json.load(file)
persons=[]
for item in data:
    person = Person(item['name'], item['age'], item['nickname'])
    persons.append(person)
for person in persons:
    print(person.name, person.age, person.nickname)