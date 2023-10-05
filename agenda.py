import sys
import os
citas ={
    "tarea":"",
    "fecha":"",
    "prioridad":""
}
agenda = []

def ordenPrio():
    alta = []
    media = []
    baja = []
    for i in agenda:
         if i["prioridad"] == "alta":
            agenda[i].append (alta)
         if i["prioridad"] == "media":
            agenda[i].append (media)
         if i["prioridad"] == "baja":
            agenda[i].append (baja)
    return (alta+media+baja)

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
    for i in agenda:
        if i["tarea"] == tarea:
            citas_a_borrar.append(i)
            print (citas_a_borrar)
    
    for cita in citas_a_borrar:
        agenda.remove(i)

def menu():
    print("------------------------cita--------------------------")
    print ("")
    print("1. añadir cita")
    print("2. borrar cita")
    print("3. buscar cita")
    print("4. ordenar por prioridad")
    print("5. cerrar agenda")
    print("_____________________________________________________")
    print ("")
    return input("que quieres hacer --> ")
    
    
def buscarCita(tarea):
    for i in agenda:
        if i["tarea"] == tarea:
            print (i["tarea"])
            print (i["fecha"])
            print (i["prioridad"])
    

if __name__ == '__main__' :
    salir = True
    while (salir == True):
        salir = menu()
        match salir:
            case "1":
                nombre_tarea = input("nombre de la cita ")
                fecha_tarea = input("Fecha de la cita ")
                prioridad_tarea = input("Prioridad de la cita ")
                addCita(nombre_tarea, fecha_tarea, prioridad_tarea)
                input ("-------------------------pulsa enter------------------------------")
                os.system ("cls")
            case "2":
                nombre_tarea = input("Dime como se llama la terea a borrar ")
                borrarCita(nombre_tarea)
                input ("-------------------------pulsa enter------------------------------")
                os.system ("cls")
            case "3":
                nombre_tarea = input("Dime como se llama la terea a buscar ")
                buscarCita(nombre_tarea)
                input ("-------------------------pulsa enter------------------------------")
                os.system ("cls")
            case "4":
                ordenPrio()
                input ("-------------------------pulsa enter------------------------------")
                os.system("cls")    
            case "5":
                salir = False
                os.system ("cls")
