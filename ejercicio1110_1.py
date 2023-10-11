number = 0
user_num = 0
while (number < 100):
    user_num = input("escribe un número: ")
    number = int(number) + int(user_num)
    if number >= 100:
        print("Se acabó!!!! Has llegado a " +str(number))
    else:
        print("la suma de los números que llevas es: "+str(number))
