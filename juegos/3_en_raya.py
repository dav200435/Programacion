cuadricula = [" "," "," "," "," "," "," "," "," "]
def visualizar ():
    print (cuadricula[0]+"|"+cuadricula[1]+"|"+cuadricula[2]+"\n")
    print(cuadricula[3]+"|"+cuadricula[4]+"|"+cuadricula[5]+"\n")
    print(cuadricula[6]+"|"+cuadricula[7]+"|"+cuadricula[8]+"\n")

def anadirValor (posicion,valor):
    cuadricula[posicion-1] = valor

def comprobar(posicion,):
    if (cuadricula[posicion-1] != " "):
        return False
    return True
def ganadora():
    if (cuadricula[0] == "x" and cuadricula[1] == "x" and cuadricula[2] == "x") or (cuadricula[3] == "x" and cuadricula[4] == "x" and cuadricula[5] == "x") or (cuadricula[6] == "x" and cuadricula[7] == "x" and cuadricula[8] == "x") or (cuadricula[0] == "x" and cuadricula[4] == "x" and cuadricula[8] == "x") or (cuadricula[2] == "x" and cuadricula[4] == "x" and cuadricula[6] == "x") or (cuadricula[0] == "x" and cuadricula[3] == "x" and cuadricula[6] == "x") or (cuadricula[1] == "x" and cuadricula[4] == "x" and cuadricula[7] == "x") or (cuadricula[1] == "x" and cuadricula[4] == "x" and cuadricula[7] == "x"):
        print("Gana jugador 1!!!")
        visualizar()
        print("Gana jugador 1!!!")
        return True
    return False

def ganadorb():
    if (cuadricula[0] == "o" and cuadricula[1] == "o" and cuadricula[2] == "o") or (cuadricula[3] == "o" and cuadricula[4] == "o" and cuadricula[5] == "o") or (cuadricula[6] == "o" and cuadricula[7] == "o" and cuadricula[8] == "o") or (cuadricula[0] == "o" and cuadricula[4] == "o" and cuadricula[8] == "o") or (cuadricula[2] == "o" and cuadricula[4] == "o" and cuadricula[6] == "o") or (cuadricula[0] == "o" and cuadricula[3] == "o" and cuadricula[6] == "o") or (cuadricula[1] == "o" and cuadricula[4] == "o" and cuadricula[7] == "o") or (cuadricula[1] == "o" and cuadricula[4] == "o" and cuadricula[7] == "o"):
        print("Gana jugador 2!!!")
        visualizar()
        print("Gana jugador 2!!!")
        return True
    return False

def empate():
    if cuadricula.count(" ") == 0:
        return True
        print("Empate!!!")
        visualizar()
        print("Empate!!!")

    return False

while (not ganadora() and not ganadorb() and not empate()):
    while True:
        visualizar()
        jugadora = int(input("donde quieres poner tu ficha jugador 1 --> "))
        if comprobar(int(jugadora),""):
            anadirValor(int(jugadora), "x")
            break
        else:
            print("Esa posición ya está ocupada, intenta de nuevo.")
        if empate():
            break

    if ganadora():
        break
    
    if empate():
        break

    while True:
        visualizar()
        jugadorb = int(input("donde quieres poner tu ficha jugador 2 --> "))
        if comprobar(int(jugadorb),""):
            anadirValor(int(jugadorb), "o")
            if (ganadorb==True):
                break
            break
        else:
            print("Esa posición ya está ocupada, intenta de nuevo.")
        
    if ganadorb():
        break
    if empate():
        break