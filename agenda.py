import sys 
import os
citas ={
    "tarea":"",
    "fecha":"",
    "prioridad":""
}
agenda = []

def addTarea(citas ,tarea):
    citas["tarea"] = tarea

def addFecha(citas ,fecha):
    citas["fecha"] = fecha

def addPrioridad(citas, prioridad):
    citas["prioridad"] = prioridad

def addCita(tarea,fecha,prioridad):
    citas_copia = citas.copy()
    addFecha(citas_copia, fecha)
    addTarea(citas_copia, tarea)
    addPrioridad(citas_copia, prioridad)
    agenda.append(citas_copia, )

def borrarCita(tarea):
    citas_a_borrar = []
    for cita in agenda:
        if cita["tarea"] == tarea:
            citas_a_borrar.append(cita)
    
    for cita in citas_a_borrar:
        agenda.remove(cita)

if __name__ == '__main__' :
    addCita ("tarea1","23/06/2023","alta")
    addCita ("tarea2","29/06/2023","media")
    addCita ("tarea3","3/10/2023","baja")
    print (agenda)
    borrarCita (input("¿Cual es el nombre de la tarea? "))
    print(agenda)