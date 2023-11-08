import time
from mando import *
distancia = controler(input("pon la ip "))
for i in range (1,11):
    distancia.action()
    time.sleep(1)
