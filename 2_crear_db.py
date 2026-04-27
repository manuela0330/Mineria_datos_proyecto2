import pandas as pd
import sqlite3

df =  pd.read_csv("omega_bruto.csv")

df_limpio= df.dropna(subset=['pmRA', 'pmDE'])

conexion= sqlite3.connect('arqueologia.db')
df_limpio.to_sql('estrellas', conexion, if_exists='replace', index=False)
conexion.close()
