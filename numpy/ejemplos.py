import numpy as np
import matplotlib.pyplot as plt

'''vector=np.arange(5)
print(vector)

matriz=np.arange(9).reshape(3,3)
print(matriz)

tensor=np.arange(12).reshape(3,2,2)
print(tensor)

a=np.array(tensor)
print(a)


b=np.array([[1,2],[3,4]])
print(b)
'''

'''print(np.linspace(start=1,stop=10,num=20))
print(np.zeros(9))
print(np.zeros((2,2)))

print(np.ones(10))

print(np.full(shape=(2,2),fill_value=5))

x=np.linspace(-500,500,20)
y=np.e**x

plt.plot(x,y)
plt.show()'''

x=np.random.rand(30,30)
'''plt.imshow(x,cmap=plt.cm.plasma )
plt.colorbar()
plt.show()'''

#grafico 3D
from mayavi import mlab

mlab.surf(x)
mlab.axes()
mlab.show()

