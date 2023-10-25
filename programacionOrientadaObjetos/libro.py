class libro:
    def __init__(self,titulo,autor,anoPublicacion,numPaginas):
        self.titulo = titulo,
        self.autor = autor,
        self.anoPublicacion = anoPublicacion,
        self.numPaginas = numPaginas
    
    def mostrarInfo(self):
        print(f"el libro {self.titulo} con autor {self.autor} y año de publicacion {self.anoPublicacion} tiene {self.numPaginas} paginas")
        
el_libro_troll = libro("el libro troll","rubius","2013",120)
el_libro_troll.mostrarInfo()