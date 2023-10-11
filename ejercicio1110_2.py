import sys
import os
user_Amount = 0
user_Fill = 0
user_Returt = 0
def menu():
    print("------------------------cita--------------------------")
    print ("")
    print("1. Hacer ingreso")
    print("2. Hacer retiro")
    print("3. Ver valance actual")
    print("4. cerrar sesión")
    print("_____________________________________________________")
    print ("")
    return input("que quieres hacer --> ")
if __name__ == '__main__' :
    salir = True
    while salir:
        salir = menu()
        match salir:
            case "1":
                user_Fill = input("¿cuanto desea agregar? ")
                user_Amount= int(user_Amount) +int(user_Fill)
                print("Se han ingresado "+str(user_Fill)+" Euros")
                input("--------------------Pulse intro para continuar--------------------")
                os.system ("cls")
            case "2":
                user_Returt = input("¿Cuanto desea retirar?")
                if int(user_Amount) < int(user_Returt):
                    print("Saldo insuficiente")
                    input("--------------------Pulse intro para continuar--------------------")
                    os.system ("cls")
                else:
                    user_Amount = int(user_Amount) - int(user_Returt)
                    print("se han retirado "+str(user_Returt)+" Euros")
                    print("el nuevo saldo es: "+ str(user_Amount))
                    input("--------------------Pulse intro para continuar--------------------")
                    os.system ("cls")
            case "3":
                print("tiene "+str(user_Amount)+" Euros en su cuenta")
                input("--------------------Pulse intro para continuar--------------------")
                os.system ("cls")
            case "4":
                salir = False
                os.system ("cls")