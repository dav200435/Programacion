import numpy as np

arr=np.loadtxt('num.txt')
print(arr)
print(arr.reshape(2,5))

arrHurricans=np.genfromtxt('Hurricanes.csv',delimiter=';')

print(arrHurricans)