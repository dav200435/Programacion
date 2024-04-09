from collections import deque

d = deque('ghi')
for elem in d:
    print(elem.upper()) #  pone el dato seleccionado en mayusculas

d.append('j')
print(d)
d.appendleft('f')
print(d)

d.pop()
print(d)
d.popleft()
print(d)

print(list(d)) # se puede usar para listar sin que se aparezca antes del array que es un deque ['g', 'h', 'i']
print(d)

print(d[0]) # se lista el primer elemento

print(d[-1]) # se lista el ultimo elemento

print(list(reversed(d)))

d.extend('jkl')
print(d)

print(d.rotate(1))

print(d.rotate(-1))

print(deque(reversed(d))) 

print(d.copy())

print(d.count('i'))

d.clear()
print(d)

try:
    d.pop()
    print(d) #aqui da error ya que el deque esta vacio y no se puede sacar un elemento de una lista que no tiene elementos
except:
    print("No hay ningun elemento en el deque")

d.extendleft('abc') #se agregan los elemntos empezando desde el ultimo al primero
print(d)