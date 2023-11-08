class Contact(list):
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
class ContactList(Contact):
    all_contact = Contact

    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in Contact.name:
                matching_contacts.append(contact)
        return matching_contacts

mario=ContactList("mario","mario@gmail.com")
dani=ContactList("dani","dani@gmail.com")
angel=ContactList("angel","angel@gmail.com")
dani.search(input("a Quien quieres buscar "))
