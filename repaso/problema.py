from collections import Counter, defaultdict, ChainMap

class Incidents:
    def __init__(self, user):
        self.incidents = defaultdict(dict)
        self.user = user
        self.clue = 1

    def insertPet(self):
        elements = self.inputPet()
        self.incidents.update(self.createDic(elements))
        self.clue += 1

    def inputPet(self):
        description = input("Introduce Descripcion de incidencia: ")
        tipe = input("Introduce tipo de incidencia: ")
        return description, tipe

    def createDic(self, elements):
        auxDic = {'clave': self.clue, 'Descripcion': elements[0], 'Tipo': elements[1],
                  'Usuario': self.user.username, 'Nombre': self.user.name}
        return auxDic

    def countTypes(self):
        count = Counter(incident['Tipo'] for incident in self.incidents.values() if isinstance(incident, dict) and 'Tipo' in incident)
        print("Tipos de incidencias y sus cantidades:")
        for tipe, num in count.items():
            print(f"{tipe}: {num}")

    def run(self):
        while True:
            print("-" * 15)
            print("1. Insertar incidencia")
            print("2. Contar tipos de incidencias")
            print("3. Salir")
            print("-" * 15)
            option = input("Seleccione una opción: ")
            try:
                option = int(option)
                if option == 1:
                    self.insertPet()
                elif option == 2:
                    self.countTypes()
                elif option == 3:
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida")
            except ValueError:
                print("Por favor, introduzca un número válido.")

class User:
    def __init__(self, name, username):
        self.name = name
        self.username = username

user = User("Mario Serradilla", "MSerradilla")
incident_manager = Incidents(user)
incident_manager.run()