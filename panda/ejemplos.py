import matplotlib.pyplot as plt
import pandas as pd

dfHurricanes=pd.read_csv('hurricanes.csv', delimiter=';')
print(dfHurricanes.to_string())
print(dfHurricanes[['name','year','deaths']].to_string())
print(dfHurricanes.tail())
print(dfHurricanes.head())

# Estadisticas

print(dfHurricanes.describe())

# Sacar info

'''print(dfHurricans.shape)
print(dfHurricans.info())
dfName=dfHurricans.set_index('name')
print(dfName.loc['Barbara'])
dfName.replace(1,2)'''

#plot = dfHurricanes.plot(x='name', y='deaths',kind='bar',title="Mueltos")
#dfHurricanes.plot(x='name',y='deaths',kind='bar',title='Deaths by Hurricanes')

#pruebas
plt.figure(figsize=(10, 6))  # Setting figure size
plt.bar(dfHurricanes['name'], dfHurricanes['deaths'])
plt.xlabel('Hurricane Name')
plt.ylabel('Number of Deaths')
plt.title('Deaths Caused by Hurricanes')
plt.xticks(rotation=270)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
#muertes anuales
muertesAnuales=dfHurricanes.groupby("years")['deaths'].sum()
plt.show 