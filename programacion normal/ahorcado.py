palabra = input("Pon una palabra --> ")
contador = 0
palabraIncognita = "_" * len(palabra)
letrasAdivinadas = ""

# Definir función para comprobar si la letra está en la palabra
def comprobarLetra(letraJugador):
    global contador
    global palabraIncognita
    letraEncontrada = False
    for i in range(len(palabra)):
        if letraJugador == palabra[i]:
            letraEncontrada = True
            palabraIncognita = palabraIncognita[i] + letraJugador + palabraIncognita[i+1]

    if letraEncontrada:
        letrasAdivinadas += letraJugador
    else:
        contador += 1
        print("Esa letra no está en la palabra. Te quedan", 6 - contador, "intentos.")

# Función para mostrar la palabra oculta y las letras adivinadas
def mostrar():
    print("Palabra adivinada:", palabraIncognita)
    print("Letras adivinadas:", letrasAdivinadas)

# Función para determinar si se ha ganado el juego
def victoria():
    return palabra == palabraIncognita

# Función para determinar si se ha perdido el juego
def perdedor():
    return contador == 6

while not (victoria(True) or perdedor(True)):
    mostrar()
    letraJugador = input("Elige una letra --> ")
    comprobarLetra(letraJugador)

if victoria():
    print("¡Felicidades! Has adivinado la palabra:", palabra)
else:
    print("¡Has perdido! La palabra era:", palabra)
