class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    
    def showContact(self):
        print(self.name,self.email)
                
class Supplier(Contact):
    def order(self, order):
        print("Si este fuera un sistema real, enviaríamos el pedido '{}' a '{}'".format(order, self.name))
        
c=Contact("jose","jose@gamil.com")
s = Supplier ("pepe","pepe@gmail.com")
s.order("Esta es la orden nnumero 101")
s.showContact()
s.order("pedido 1")
for i in Contact.all_contacts:
    print(i.name,i.email)