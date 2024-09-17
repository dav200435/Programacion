import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ej1():
    notas = np.array([7,6,4,8,1])
    
    media=0
    mayor = 0
    menor = 0
    
    for i in notas:
        print(i)
        media +=i
        if menor>i:
            menor=i
        if mayor<i:
            mayor=i
    media =media/notas.__len__()
    print(f"media:{media}, Menor:{menor}, Mayor:{mayor} ")
    
    
def ej2():
    diagonal=np.arange(25).reshape(5,5)
    i=0
    while i<diagonal.__len__():
        for j in range(0,diagonal[i].__len__()):
            if j == i:
                diagonal[i][j]=1
            else:
                diagonal[i][j]=0
        i+=1
    print(diagonal)
    
    
def ej3():
    dataframe=pd.read_csv('AppleStore.csv',delimiter=',')
    print(dataframe.to_string())
    print(dataframe.describe)
    numeric_columns = dataframe.select_dtypes(include=['float64', 'int64'])
    print(numeric_columns.corr())
    print("precio ",dataframe["price"].mean())
    print("bytes ",dataframe["size_bytes"].mean())
    print("precio superior a 4.5 ", dataframe["price"][dataframe["user_rating"]>=4.5].mean())
    
    pd.plotting.scatter_matrix(numeric_columns,figsize=(11,11),alpha=0.5)
    plt.show()
    # se muestra una relacion entre todos los datos numericos
    # se muestran las posibles relaciones entre los datos del documento
    
    
    priceRating = pd.pivot_table(dataframe, index='price', columns='user_rating', aggfunc='size', fill_value=0)
    priceRating.plot(kind='bar', stacked=True)
    plt.show()
    # se muestra una grafica entre las valoraciones de los usuarios y el precio
    # se muestra la relacion entre las reseñas de los usuarios segmentado en precios, 
    # en las aplicaciones muy caras no hay valoraciones en cambio en las varatas hay muchas
    
    tipeprice = pd.pivot_table(dataframe, index='prime_genre', columns='price', aggfunc='size', fill_value=0)
    tipeprice.plot(kind='bar', stacked=True)
    plt.show()
    # se muestra la relacion entre el precio y el tipo de aplicacion
    # se muestra como x tipo de aplicacion suelen ser gratuitas al usuario como las redes sociales 
    # en cambio otras mas especificas son de pago

ej1()
input("presiona intro para continuar al ejercicio 2-> ")
ej2()
input("presiona intro para continuar al ejercicio 3 -> ")
ej3()