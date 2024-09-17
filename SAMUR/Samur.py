from Action import Action
from ActionLst import ActionsLst
from DBUtils import DBUtils

import pandas as pd

class Samur:
    def __init__(self):
        self.file = "./activaciones_samur_2023.csv"
        self.dataframe = pd.read_csv(self.file, sep=';', encoding='utf-8-sig')
        self.dataframe.columns = [col.strip() for col in self.dataframe.columns]  # Elimina espacios en blanco alrededor de los nombres de las columnas
        self.dataframe.rename(columns={
            'Anio': 'Año',
            'Hora IntervenciÃ³n': 'Hora Intervención',
            'CÃ³digo': 'Código'
        }, inplace=True)
        print("Columnas del DataFrame:", self.dataframe.columns)  # Imprime los nombres de las columnas
        self.ActionLst = ActionsLst()
        self.db = DBUtils()
    
    def get_actions(self):
        for index, row in self.dataframe.iterrows():
            action = Action(
                anio=row['Año'] if pd.notna(row['Año']) else None,
                mes=row['Mes'] if pd.notna(row['Mes']) else None,
                horaSolicitud=row['Hora Solicitud'] if pd.notna(row['Hora Solicitud']) else None,
                horaIntervencion=row['Hora Intervención'] if pd.notna(row['Hora Intervención']) else None,
                cod=row['Código'] if pd.notna(row['Código']) else None,
                distrito=row['Distrito'] if pd.notna(row['Distrito']) else None,
                hospital=row['Hospital'] if pd.notna(row['Hospital']) else None
            )
            self.ActionLst.addAction(action)
        self.db.insert(self.ActionLst.getList())