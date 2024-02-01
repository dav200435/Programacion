import pyttsx3

texto = open(r"fichero.txt")

texto_linea=texto.readlines()
    
engine=pyttsx3.init()

for linea in texto_linea:
    engine.say(linea)
    engine.runAndWait()