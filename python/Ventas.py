import pandas as pd
import os

# Ruta del directorio que contiene los archivos CSV
ruta_archivos = r'C:\Users\majov\Desktop\ventas\Archivos'

# Obtener la lista de archivos CSV en el directorio
archivos_csv = [archivo for archivo in os.listdir(ruta_archivos) if archivo.endswith('.csv')]

# Inicializar una lista vacía para almacenar los DataFrames de cada archivo
lista_dataframes = []

# Iterar sobre cada archivo CSV, cargarlo y añadirlo a la lista de DataFrames
for archivo in archivos_csv:
    ruta_completa = os.path.join(ruta_archivos, archivo)
    df = pd.read_csv(ruta_completa)
    lista_dataframes.append(df)

# Concatenar todos los DataFrames en uno solo
datos_completos = pd.concat(lista_dataframes, ignore_index=True)

# Mostrar los primeros registros del DataFrame concatenado
print("Primeros registros de los datos concatenados:")
print(datos_completos.head())

# Mostrar los nombres de los archivos en el directorio
print("\nArchivos en el directorio:")
for archivo in archivos_csv:
    print(archivo)

# Mostrar los nombres de los archivos en una tabla
print("\nTabla de nombres de archivos:")
print("-" * 30)
print("| {:<20} |".format("Nombre del Archivo"))
print("-" * 30)
for archivo in archivos_csv:
    print("| {:<20} |".format(archivo))
print("-" * 30)

# Conteo de valores nulos por columna
conteo_nulos = datos_completos.isnull().sum()
print("Conteo de valores nulos por columna:")
print(conteo_nulos)

# Mostrar tipos de datos de cada columna
tipos_variables = datos_completos.dtypes
print("\nTipos de datos de cada variable:")
print(tipos_variables)


import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que ya has cargado tus datos y agrupado por mes como se mencionó anteriormente
# Ejemplo de agrupación por mes y sumar las ventas
# ventas_por_mes = datos_completos.groupby(datos_completos['Order Date'].dt.month)['Quantity Ordered'].sum()

# Ejemplo para demostrar la definición de ventas_por_mes (reemplaza esto con tu lógica real)
ventas_por_mes = pd.Series([100, 150, 200, 180, 250, 300, 280, 310, 270, 320, 350, 380], index=range(1, 13))

# Mostrar el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(ventas_por_mes.index, ventas_por_mes.values, color='skyblue')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Ventas por Mes')
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que ya has cargado tus datos y agrupado por ciudad como se mencionó anteriormente
# Ejemplo de agrupación por ciudad y sumar las ventas
# ventas_por_ciudad = datos_completos.groupby('Ciudad')['Ventas'].sum()

# Ejemplo para demostrar la definición de ventas_por_ciudad (reemplaza esto con tu lógica real)
ventas_por_ciudad = pd.Series({'Ciudad A': 5000, 'Ciudad B': 7000, 'Ciudad C': 3000, 'Ciudad D': 6000})

# Mostrar el gráfico de barras horizontales de ventas por ciudad
plt.figure(figsize=(10, 6))
ventas_por_ciudad.sort_values().plot(kind='barh', color='lightgreen')
plt.xlabel('Ventas')
plt.ylabel('Ciudad')
plt.title('Ventas por Ciudad')
plt.grid(True)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generar fechas para todo un año (365 días)
fecha_inicio = pd.Timestamp('2023-01-01')
fecha_final = pd.Timestamp('2023-12-31')
fechas = pd.date_range(start=fecha_inicio, end=fecha_final)

# Generar datos ficticios para las ventas diarias (solo como ejemplo)
np.random.seed(0)  # Para reproducibilidad del ejemplo
ventas_diarias = np.random.randint(50, 300, size=len(fechas))  # Generar datos aleatorios

# Crear la Serie de ventas por fecha
ventas_por_fecha = pd.Series(index=fechas, data=ventas_diarias)

# Mostrar el gráfico de líneas de ventas por fecha
plt.figure(figsize=(12, 6))
ventas_por_fecha.plot(kind='line', marker='o', color='orange')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.title('Ventas Diarias')
plt.grid(True)
plt.show()


import pandas as pd


#*******

import pandas as pd
import numpy as np

# Generar fechas para todo un año (365 días)
fecha_inicio = pd.Timestamp('2023-01-01')
fecha_final = pd.Timestamp('2023-12-31')
fechas = pd.date_range(start=fecha_inicio, end=fecha_final)

# Generar datos ficticios para las ventas diarias (solo como ejemplo)
np.random.seed(0)  # Para reproducibilidad del ejemplo
ventas_diarias = np.random.randint(50, 300, size=len(fechas))  # Generar datos aleatorios

# Crear un DataFrame con las fechas y las ventas diarias
ventas_por_fecha = pd.DataFrame({
    'Fecha': fechas,
    'Ventas': ventas_diarias
})

# Mostrar una tabla con los datos de ventas por fecha
print("\nTabla de ventas por fecha:")
print("-" * 30)
print(ventas_por_fecha.head().to_string(index=False))  # Mostrar los primeros registros sin índice
print("-" * 30)

# ****

from dash import Dash, html
from dash.dash_table import DataTable
import pandas as pd

# Datos de ejemplo
datos = {
    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Ventas': [222, 97, 167, 242, 117]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Iniciar la aplicación Dash
app = Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div([
    html.H1("Tabla de Ventas"),
    DataTable(
        id='tabla-ventas',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
