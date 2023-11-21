class errores:
    def __init__(self):
        pass
    def error3 (self):
      
        try:
            lista = [1, 2, 3]
            print(lista[3])
        except IndexError as e:
            print(f"Error de índice: {e}")
        except Exception as e:
            print(f"Otro error: {e}")
          
    def error4(self):
        try: numero = int(input("Ingresa un número: ")) 
        except ValueError: print("Eso no es un número válido.") 
        else: print(f"Has ingresado el número {numero}") 
        finally: print("Fin del bloque try-except")
            
hola = errores()
res = hola.error4()
print("El resultado es:")
print(res)