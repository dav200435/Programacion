import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ¿Cuántas filas y columnas? a través del dataframe muestra estsa información
seasons=pd.read_csv('all_seasons.csv',delimiter=',')
#print(seasons.to_string())
print(seasons.info())

# Crea un índice de la columan season
print(seasons.set_index('season'))

# Cuenta los valores de la columna edad. value_conts()
print(seasons.value_counts(['age']))

# Paso 2: Quitar valores NULL (o valores nulos)
seasons.dropna(inplace=True)
seasons.shape
# ¿Cuántas filas y columnas? a través del dataframe muestra estsa información ahora.
print(seasons.info())

# Saca la media de edad de los jugadores. mean()
print(seasons['age'].mean())

# Saca la media de edad los jugadores estadounidenses
print(seasons['age'][seasons["country"] == "USA"].mean())

# Paso 3: Undrafted. Jugadores que no han sido elegidos a través de este sorteo, a lo largo de la historia 
# se han desarrollado varios “robos” o jugadores que han dejado huella en la liga,
UndraftRound= seasons[seasons['draft_round']=='Undrafted']
seasons['draft_round']=seasons['draft_round'].replace('Undrafted',np.NaN)
print(UndraftRound)
undraftNum=seasons[seasons['draft_number']=='Undrafted']
seasons['draft_number']=seasons['draft_number'].replace('Undrafted',np.NaN)
print(undraftNum)

# Paso 4: Muestra las estadísticas de la tabla
print(seasons.describe())

# Paso 5: Seleccionamos las columnas
col_need=['age','player_height','player_weight','gp','pts','reb','ast','net_rating','oreb_pct','dreb_pct','usg_pct','ts_pct','ast_pct']
ana_df=seasons[col_need]
ana_df
ana_df.duplicated().values.any()
print(ana_df.to_string())

# Paso 6: Muestra tu tabla de correlación a partir del dataframe ana_df
ana_dfCorr=ana_df.corr()
print(ana_dfCorr)

# Paso 7: Muestra la gráfica de la correlación
plt.xticks(rotation=270)
pd.plotting.scatter_matrix(ana_dfCorr,figsize=(20,20),alpha=0.5)
plt.show()
# Prueba esta visualización. 

sns.pairplot(ana_dfCorr)
plt.show()

#¿Cuál es mejor? ¿ Por qué?

sns.countplot(x="player_weight", hue="player_height", data=ana_dfCorr)
plt.show()