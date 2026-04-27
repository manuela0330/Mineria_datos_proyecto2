import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conexion= sqlite3.connect('arqueologia.db')
consulta="SELECT pmRA, pmDE, Gmag, BPmag, RPmag FROM estrellas"

#esta es la sección 4 de la parte 4, se hace aquí de una vez para no tener que volver a hacer una conexión.

filtro1 = "SELECT * FROM estrellas WHERE pmRA BETWEEN -7 AND 0 AND pmDE BETWEEN -10 AND -3 "
df_cluster1 = pd.read_sql_query(filtro1, conexion)

df_3= pd.read_sql_query(consulta, conexion)
print(df_3)
conexion.close()


plt.figure(figsize=(8,5))
plt.scatter(df_3['pmRA'], df_3['pmDE'], s=2, color='black', alpha=0.3)

plt.title('Movimiento propio')
plt.xlabel('Movimiento propio en AR')
plt.ylabel('Movimiento propio en DEC')

plt.axhline(0, color='red', linestyle='--', alpha=0.5)
plt.axvline(0, color='red', linestyle='--', alpha=0.5)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
plt.savefig('movimiento_propio.png')
print("Gráfica 1 guardada como 'movimiento_propio.png'")


#ahora se hace la gráfica del diagrama H-R
#para primer cúmulo detectado
df_cluster1['color_index'] = df_cluster1['BPmag'] - df_cluster1['RPmag']
plt.style.use('dark_background')
plt.figure(figsize=(8, 10)) 
plt.scatter(df_cluster1['color_index'], df_cluster1['Gmag'],c=df_cluster1['color_index'], cmap='RdYlBu_r', s=1, alpha=0.9)
plt.colorbar(label='Temperatura (Azul = Caliente, Rojo = Frío)')
plt.gca().invert_yaxis()
plt.title('Diagrama Color-Magnitud: Omega Centauri (Filtrado)')
plt.xlabel('Índice de Color (BP - RP)')
plt.ylabel('Magnitud G (Brillo)')
plt.grid()
plt.savefig('diagrama_hr_omega.png')
print("Gráfica 2 guardada como 'diagrama_hr_omega.png'")

#para segundo cúmulo detectado
#df_cluster2['color_index'] = df_cluster2['BPmag'] - df_cluster2['RPmag']
#plt.style.use('dark_background')
#plt.figure(figsize=(8,10))
#plt.scatter(df_cluster2['color_index'], df_cluster2['Gmag'], s=1, color='purple', alpha=0.5)
#plt.gca().invert_yaxis()
#plt.title('Diagrama Color-Magnitud')
#plt.xlabel('índice de color (BP - RP)')
#plt.ylabel('Magnitud G (brillo)')
#plt.grid()
#plt.savefig('diagrama1_hr_omega.png')
#print("Gráfica 3 guardada como 'diagrama1_hr_omega.png")


