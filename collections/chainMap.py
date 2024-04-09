from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}

adjustments = {'art': 'van gogh', 'opera': 'carmen'}

print(list(ChainMap(adjustments, baseline))) 
# en caso de haber un valor repetido se selecciona el primero que sale

combined = baseline.copy() # se usa para copiar diccionarios

combined.update(adjustments) 
# con update selecciona los datos repetidos del segundo diccionario
print(combined)

print(list(combined)) # con list solo se ven las claves

c = ChainMap() # Crea el contexto raíz
d = c.new_child() # Crea un contexto secundario anidado
e = c.new_child() # Contexto hijo de c, independiente de d
e.maps[0] # Diccionario de contexto actual, similar a locals() en Python
e.maps[-1] # Contexto raíz, similar a globals() en Python
e.parents # Cadena de contextos de encierro, similar a nonlocals en Python

d['x'] = 1 # Establece el valor en el contexto actual
d['x'] # Obtiene la primera clave en la cadena de contextos
del d['x'] # Elimina del contexto actual
list(d) # Todos los valores anidados
len(d) # Número de valores anidados
d.items() # Todos los elementos anidados
dict(d) # Convierte en un diccionario regular