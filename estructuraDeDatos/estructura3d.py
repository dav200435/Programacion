import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las coordenadas de los vértices del cubo
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Definir las aristas del cubo
aristas = [[vertices[0], vertices[1], vertices[2], vertices[3], vertices[0]],
           [vertices[4], vertices[5], vertices[6], vertices[7], vertices[4]],
           [vertices[0], vertices[4]],
           [vertices[1], vertices[5]],
           [vertices[2], vertices[6]],
           [vertices[3], vertices[7]]]

# Convertir las listas de coordenadas de los vértices y aristas en arrays numpy
vertices = np.array(vertices)
aristas = [np.array(arista) for arista in aristas]  # Convertir cada sublista en un array numpy

# Crear una figura y un subplot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar las aristas
for arista in aristas:
    x = arista[:, 0]
    y = arista[:, 1]
    z = arista[:, 2]
    ax.plot(x, y, z, color='b')

# Configurar etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
