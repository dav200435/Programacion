class persona:
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class profesor(persona):
    
    def __init__(self, numEmpleado):
        self.numEmpleado = numEmpleado
    
    def profesor(self):
        print(f"nombre " + {self.nombre} + " edad "+{self.edad}+" dni "+{self.dni} +" numero de empleado "+{self.numEmpleado})

class Estudiante(persona):
   
    def __init__(self, matricula):
        self.matricula = matricula
       
    def informacion(self):
        print(f'{"Nombre: " + self.nombre}')
        print(f'{"Edad: " + self.edad}')
        print(f'{"DNI: " + self.dni}')
        print(f'{"Matrícula: " + self.matricula}')