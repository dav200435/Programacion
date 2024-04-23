from collections import ChainMap

dic1={'La': 1, 'noche': 1, 'envuelve': 1, 'la': 2, 'ciudad': 1, }
dic2={'La': 1, 'noche': 1, 'envuelve': 1, 'la': 2, 'ciudad': 1, }
dic3={'La': 1, 'noche': 1, 'envuelve': 1, 'la': 2, 'ciudad': 1, }
mapa=ChainMap(dic1,dic2,dic3)
#print(mapa)
lista1=list(mapa.values())
lista2=list(mapa.keys())
print(lista1)
print(lista2)