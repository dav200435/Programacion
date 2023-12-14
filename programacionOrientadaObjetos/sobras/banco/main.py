from cuentas import CuaentaBancaria

cliente1 = CuaentaBancaria("persona1")

cliente2 = CuaentaBancaria("persona2")

cliente3 = CuaentaBancaria("persona3")

def menu():
    print("------------------------cita--------------------------")
    print ("")
    print("1. Cuenta 1")
    print("2. Cuenta 2")
    print("3. Cuenta 3")
    print("4. Salir")
    print("_____________________________________________________")
    print ("")
    return input("que quieres hacer --> ")

def menuUsuario():
    print("------------------------cita--------------------------")
    print ("")
    print("1. Hacer ingreso")
    print("2. Retirar dinero")
    print("3. Salir")
    print("_____________________________________________________")
    print ("")
    return input("que quieres hacer --> ")

if __name__ == "__main__":
    salir = True
    while salir:
        salir = menu()
        match salir:
            case "1":
                salir = menuUsuario()
                match salir:
                    case"1":
                        cliente1.depositar()
                    case"2":
                        cliente1.retirar()
                    case"3":
                        salir=False
            case "2":
                salir = menuUsuario()
                match salir:
                    case"1":
                        cliente2.depositar()
                    case"2":
                        cliente2.retirar()
                    case"3":
                        salir=False
            case "3":
                salir = menuUsuario()
                match salir:
                    case"1":
                        cliente3.depositar()
                    case"2":
                        cliente3.retirar()
                    case"3":
                        salir=False
            case"4":
                salir=False