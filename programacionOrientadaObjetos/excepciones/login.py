class loginError(Exception):
        pass
    
class login:
    def __init__(self,user,passwd) -> None:
        self.user = user
        self.passwd = passwd
    
    def validalogin(self,user,passwd):
        if self.user == user and self.passwd == passwd:
            print("OK")
        else:
            raise loginError("Usuario o contraseña invalido")
        
l=login("pepe","1234")
try:
    l.validalogin("pepe","123")
except loginError as e:
    print(e)