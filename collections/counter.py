from collections import Counter

'''
c= Counter(['a','a','a','h','f','b','h','e','s','b','c','s','s','d','h','h','f',])
print(c)
'''

def ej1():
    dic = {}
    veces = int(input("¿Cuántos elementos quieres insertar? -> "))
    
    for i in range(veces):
        clave = input("Inserta clave-> ")
        valor = input("Inserta valor-> ")
        dic[clave] = int(valor)
    
    print(dic)
    final = Counter(dic)
    print(list(final.elements()))
    


def ej2():
    frase=input("inserta la frase-> ")
    lista=frase.split()
    count=Counter(lista).most_common()
    print(count)
    
def quijote():
    veces=input("cuatas palabras mas repetidas deseas ver-> ")
    with open("el_quijote.txt","r",encoding="iso-8859-1") as file:
        quijote=file.read()
        array=quijote.split()
        contador=Counter(array).most_common(int(veces))
        print(contador)
    
'''ej1()
ej2()'''
quijote()