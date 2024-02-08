import requests

class serializacionWeb:
    
    def solicitar(self):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        return response.json()
    
    def crear(self):
        elements = []
        data = self.solicitar() 
        for element in data:
            elements.append(elemento(element['userId'], element['id'], element['title'], element['completed']))
        self.mostrar(elements)
    
    def mostrar(self, elements): 
        for element in elements:
            print('userId:',element.userId,'id:' ,element.id,'title:', element.title,'completed:', element.completed,'\n')

class elemento:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

serializacionWeb().crear()