import os
def virus():
    direccion = os.getcwd()
    infectados_dir = os.path.join(direccion, "infectados")

    if not os.path.exists(infectados_dir):
        os.mkdir(infectados_dir)

    files = os.listdir()

    for file_name in files:
        if file_name.endswith(".txt"):
            file_path = os.path.join(infectados_dir, file_name)
            
            with open(file_path, "w") as g:
                g.write("Infectado")
                
virus()