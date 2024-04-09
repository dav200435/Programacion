from collections import defaultdict

with open("el_quijote.txt","r",encoding="iso-8859-1") as frase:
    fra=frase.read()
    separado=fra.split(" ")
    letter_counter=defaultdict(int)
    for word in separado:
        letter_counter[word] +=1
print(letter_counter)
