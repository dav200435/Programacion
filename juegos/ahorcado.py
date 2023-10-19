palabra = input("Pon una palabra --> ")
contador = 0
palabraIncognita = ""
letraJugador = ""
contadorInverso = 6 - contador
letrasAdivinadas = ""
#definir comprobacion de letra con un bucle que revise la posicion en la que esta si la letra existe
def comprobarLetra(letraJugador):
    global contador
    letraEncontrada = False
    for i in range(len(palabra)):
        if letraJugador == palabra[i]:
            letrasAdivinadas[i] = letraJugador
            letraEncontrada = True
    if not letraEncontrada:
        contador += 1
        print("Esa letra no está en la palabra. Te quedan", str(contadorInverso), "intentos.")

def convertirpalabra(palabra):
    palabraIncognita = '_' * len(palabra)
    return palabraIncognita


def mostrar():
    print(letrasAdivinadas)
    convertirpalabra()

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
