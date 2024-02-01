import python_filmaffinity
service = python_filmaffinity.FilmAffinity()

movies=service.top_netflix()
fichero=open("peliculas.txt","w")
fichero.write("MEJORES PELICULAS DE NETFLIX \n\n")
for i in movies:
    fichero.write(i['title'])
    fichero.write("     Directores:     ")
    fichero.write(str(i['directors']))
    fichero.write("\n")
fichero.close