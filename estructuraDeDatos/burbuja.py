array = [5,45,84,34,15,54,2,4,1,7,3,468,135,786,16,875,31,65,0]
for i in range (0,len(array)-1):
    for j in range (0,len(array)-1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)