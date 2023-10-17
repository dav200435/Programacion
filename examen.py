import os
def ejercicio1():
    n1=input("introduce un numero ")
    n2=input("introduce un numero ")
    n3=input("introduce un numero ")
    n4=input("introduce un numero ")
    n5=input("introduce un numero ")
    n6=input("introduce un numero ")
    n7=input("introduce un numero ")
    n8=input("introduce un numero ")
    n9=input("introduce un numero ")
    n10=input("introduce un numero ")
    total = int(n1)+int(n2)+int(n3)+int(n4)+int(n5)+int(n6)+int(n7)+int(n8)+int(n9)+int(n10)
    print(total)
def ejercicio2():
    suma = 0
    for i in range (1,200):
        if i%2 != 0:
            suma=i+int(suma)
    print(suma)
def ejercicio3():
    cuantia = input("cuantos numeros quieres poner ")
    lista = []
    suma = 0
    resultado = 0
    for i in range (0,int(cuantia)):
        dato= input("mete un numero")
        lista.append(dato)
    for i in range (0,len(lista)):
        suma = int(lista[i])+int(suma)
    resultado = suma/int(cuantia)
    print(resultado)
def ejercicio4():
    palabras = [25,15,12,10,5,9,1,2,3,4,6,7,8]
    comprobar = input("que numero quieres comprobar si esta")
    for i in range (0,len(palabras)):
        if int(comprobar) == int(palabras[i]):
            print("tu numero esta en la lista")
            break    
        print("tu numero no esta en la lista")
def ejercicio5():
    cont_vocales = 0
    consonantes = 0
    palabra = input("introduce una palabra ")
    vocales = ("a","e","i","o","u")
    for i in range (0,len(palabra)):
        if palabra[i] in vocales:
            cont_vocales +=1
        else:
            consonantes +=1
    print("hay "+str(cont_vocales)+" vocales")
    print("hay "+str(consonantes)+" consonantes")
def ejercicio6():
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
        while salir:
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
                    salir = False
                    os.system ("cls")

def ejercicio7():
    temperatura = input("dame la temperatura ")
    temperatura = int(temperatura) * 1.8 + 32
    print (str(temperatura)+"ºf")

def ejercicio8():
    metros = input("Dame la distancia en metros ")
    kilometros = int(metros)/1000
    print(str(metros) + " metros son " + str(kilometros)+" kilometros")

def ejercicio9():
    texto = input("pon un texto ")
    buscar = ("(",")")
    contador = 0
    for i in range (0,len(texto)):
        if texto[i] in buscar:
            contador += 1
    print("Hay "+str(contador)+" aperturas y cierres de parentesis")

def ejercicio10():
    lista = input("pon una frase ")
    caracter = input("que caracter quieres buscar ")
    for i in range (0,len(lista)):
        if caracter == lista[i]:
            print("se encuentra en la posición "+str(i))
        else:
            print("no se encontro en la posición "+str(i))

ejercicio1()
input("pulsa intro")
ejercicio2()
input("pulsa intro")
ejercicio3()
input("pulsa intro")
ejercicio4()
input("pulsa intro")
ejercicio5()
input("pulsa intro")
ejercicio6()
input("pulsa intro")
ejercicio7()
input("pulsa intro")
ejercicio8()
input("pulsa intro")
ejercicio9()
input("pulsa intro")
ejercicio10()
input("pulsa intro")