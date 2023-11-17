from abc import ABC, abstractmethod
import random
probabilidad = random.random()

class arma (ABC):
    
    @abstractmethod
    def update(self):
        pass
    
    def usar(self):
        pass

class pistola (arma):
    def __init__(self,numBalas,daño):
        self.cargador=numBalas
        self.balitas = self.cargador
        self.daño = daño
        
        
    
    def update(self):
        print("he")

    def usar(self,balas):
        if balas>0:
            print ("pium")
            self.cargador = self.cargador -1
            return self.cargador
        else:
            print("I need more bullets")
        
    def recargar(self):
        self.cargador = self.balitas
        return self.cargador

class jugador:
    def __init__(self, vida):
        self.vida = vida
        
class enemigo:
    def __init__(self, vida, daño):
        self.vida = vida
        self.enemyDaño = daño
        

class juego:
    def __init__(self, arma, player, enemy):
        self.arma = arma
        self.player = player
        self.enemy = enemy
    
    def jugar(self, arma):
        
        while True:
            print(f"Te quedan {player.vida} puntos de vida")
            print(f"Le quedan {enemy.vida} puntos de vida")

            if player.vida <= 0:
                print("¡HAS PERDIDO!")
                return False

            if enemy.vida <= 0:
                print("¡HAS GANADO!")
                return False

            accion = input("¿Qué quieres hacer? Disparar (d), recargar (r) o salir (s): ")

            if accion == "d":
                if pistol.cargador > 0:
                    if probabilidad < 0.6:
                        print("¡HAS ACERTADO!")
                        enemy.vida -= pistol.daño
                    else:
                        print("¡FALLASTE!")
                pistol.usar(pistol.cargador)

            elif accion == "r":
                arma.recargar()

            elif accion == "s":
                return False

            else:
                print("Acción no reconocida")

            player.vida -= enemy.enemyDaño
  

pistol = pistola(7,6)
player = jugador(50)
enemy = enemigo(60,4)
play = juego(pistol,player,enemy)
play.jugar(pistol)
