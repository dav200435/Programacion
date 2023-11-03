class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    def order(self, order):
        print("Si este fuera un sistema real, enviaríamos el pedido '{}' a '{}'".format(order, self.name))
        

angel = Supplier("angel","angel@gmail.com",1)
print(Contact.all_contacts)