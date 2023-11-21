from typing_extensions import LiteralString
palabra = input("Pon una palabra --> ")
contador = 0
palabraIncognita = ""
letraJugador = ""
contadorInverso = 6 - contador
letrasAdivinadas = ""
letraEncontrada = False
#definir comprobacion de letra con un bucle que revise la posicion en la que esta si la letra existe
def comprobarLetra(letraJugador):
    global contador
    letraEncontrada = False
    i = 0
    for i in range(len(palabra)):
        if letraJugador == palabra[i]:
            letraEncontrada = True
            letraJugador = letrasAdivinadas
            letraJugador = palabraIncognita[i]
    if (letraEncontrada== False):
        print("Esa letra no está en la palabra. Te quedan", str(contadorInverso), "intentos.")
        contador += 1
def convertirpalabra(palabra):
    guiones = "_" * len(palabra)
    print(guiones)


def mostrar():
    print(letrasAdivinadas)
    print(convertirpalabra)

def victoria():
    if (palabra == palabraIncognita):
        return True
    else:
        return False
def perdedor():
    if contadorInverso==0:
        print("Habeis perdido. Si juegas solo eres muy triste para no acertarr tu propia palabra ve al medico para que te vean ese alzheimer")
        return True
    return False

while ((victoria() == False) and (perdedor() == False)):
    victoria()
    perdedor()
    mostrar()
    letraJugador = input("elige una letra --> ")
    comprobarLetra(letraJugador)