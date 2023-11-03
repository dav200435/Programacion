import time
from mando import *
distancia = mando(input("pon la ip "))
for i in range (1,11):
    distancia.action()
    time.sleep(0.4)
