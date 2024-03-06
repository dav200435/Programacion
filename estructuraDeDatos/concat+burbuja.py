array1=[1,3,5,7]
array2=[2,6,8,10]

for i in array2:
    array1.append(i)
    
for i in range (0,len(array1)-1):
    for j in range (0,len(array1)-1):
        if array1[j] > array1[j + 1]:
            array1[j], array1[j + 1] = array1[j + 1], array1[j]

print(array1)