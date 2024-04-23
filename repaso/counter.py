from collections import Counter

parrafo="La noche envuelve la ciudad con su manto oscuro, salpicado de destellos de luz que danzan en las calles. Entre el bullicio de la urbe, se escuchan susurros de historias por descubrir, mientras el tiempo se desvanece entre las sombras, dejando atrás un rastro de misterio y nostalgia."
parrafo2="La noche envuelve la ciudad con su manto oscuro, salpicado de destellos de luz que danzan en las calles. Entre el bullicio de la urbe, se escuchan susurros de historias por descubrir, mientras el tiempo se desvanece entre las sombras, dejando atrás un rastro de misterio y nostalgia."

def ej1():
    c=Counter(parrafo.lower().split(" "))
    print(c)

#fichero
def ej2():
    with open('el_quijote.txt','r',encoding="iso-8859-1") as f:
        c=Counter(f.read().split(" "))
        print(c)

#busca palabra y que encuentre cuantas veces sale
def ej3():
    c=Counter(parrafo.lower().split(" "))
    print(c.get("la"))

#recorre dic collections para que salga palabra que mas veces sale texto

def ej4():
    c=Counter(parrafo.lower().split(" "))
    for palabra, frecuencia in c.items():
        if palabra == "la":
            print(frecuencia)
            break

#obtener palabra mas comun
def ej5():
    c=Counter(parrafo.lower().split(" ")).most_common(1)
    print(c)

#junta los 2 diccionarios sumando las palabras que se repitan
def ej6():
    c=Counter(parrafo.lower().split(" "))
    d=Counter(parrafo2.lower().split(" "))
    print(c.update(d))
