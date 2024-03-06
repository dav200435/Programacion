usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

cont = 0
loggedin = False
while cont<3 and not loggedin:
    user = input("Introduce usuario: ")
    passwd = input("Introduce contraseña: ")
    if user in usuarios and usuarios[user]["password"] == passwd:
        print(usuarios[user]["nombre"], usuarios[user]["apellido"])
        loggedin = True
    else:
        print(False)
        cont += 1

if not loggedin:
    print("Límite de intentos alcanzado.")
