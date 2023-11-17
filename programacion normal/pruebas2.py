import sys 
import os
citas ={
    "fecha":"",
    "tarea":"",
    "prioridad":""
    }
while (True):
    match menu:
        case "1":
            cita["fecha"]= input("dame la fecha ")
            cita["tarea"]= input("dame la tarea ")
            cita["prioridad"]= input("dame la prioridad(alto, medio, bajo) ")
            #mandas tarea