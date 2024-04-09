import array
import binascii

numlist=[1,8,7,6,4,2,7]
numlistf=[1,8.6,7.1,6.1,4.8,2.5,7.4]
arr1=array.array('b',numlist)
arr2=array.array('B',numlist)
floats=array.array('f',numlistf)
anadido=7
anadido2=7,13,25

s = b'Esto es un array de texto'
a=array.array('b',s)
print(f"byte string: {a}")
print(f"como array: {s}")
print(f"como exadecimal: {binascii.hexlify(a)}")

print(arr1.tolist())

print(floats)

print(arr2.typecode)
print(arr2.itemsize)

print(arr2.tolist())
arr2.append(anadido)
print(arr2.tolist())
arr2.extend(anadido2)
print(arr2.tolist())
print(arr2.__len__())
print(arr2.index(25))
arr2.insert(4,anadido)
print(arr2.tolist())
print(arr2.pop(5))
arr2.reverse()
print(arr2.tolist())
arr2.pop(arr2.index(6))
print(arr2.tolist())
print(arr2[3])



array_one = array.array("u", ['a','b','c','d'])

array_two = array.array("u", ['e','f','g'])

with open('salida.txt','wb') as f:

    print (array_one)
    array_one.tofile(f)

    print (array_two)
    array_two.tofile(f)

with open('salida.txt','r')as f:
    text = f.read()
    text.split()
    print(text)
    arr=array.array('u',text)
    print(arr.tolist())