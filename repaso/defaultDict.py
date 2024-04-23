from collections import defaultdict

ciudades = [('Madrid', 'M'), ('Salamanca', 'SA'), ('Barcelona', 'B'), ('Valencia', 'V')]
parrafo2="La noche envuelve la ciudad con su manto oscuro, salpicado de destellos de luz que danzan en las calles. Entre el bullicio de la urbe, se escuchan susurros de historias por descubrir, mientras el tiempo se desvanece entre las sombras, dejando atrás un rastro de misterio y nostalgia."

def ej1():
    defdict = defaultdict(list)
    for i in ciudades:
        defdict[i[0]].append(i[1])

    print(defdict)

def ej2():
    defdict = defaultdict(int)
    for elemento in parrafo2.split(" "):
        defdict[elemento] += 1

    print(defdict)
    
