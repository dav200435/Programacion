def crear():
    textoInicial='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body>'
    fichero=open("fichero.txt","r")
    pagina=open("pagina.html","a")
    filas=fichero.readlines()
    pagina.write(textoInicial)
    for i in range(len(filas)):
        pagina.write('<p>'+filas[i]+'</p>')
    
    final=("</body></html>")
    pagina.write(final)
    fichero.close()
    pagina.close()

crear()