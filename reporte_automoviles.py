import pandas as pd
from ydata_profiling import ProfileReport

# Ruta de los datos
DATOS_DIR = 'C:/Users/Peter/Desktop/all/Facu/Mineria De Datos Usando Sistemas Inteligentes/Datos/'

# Cargar el dataset
df = pd.read_csv(DATOS_DIR + 'automobile.csv')

# Crear el reporte
print("Generando reporte del dataset...")
profile = ProfileReport(df, title="Reporte de Análisis de Automóviles", explorative=True)

# Guardar el reporte en HTML
profile.to_file("reporte_automoviles.html")
print("Reporte generado exitosamente como 'reporte_automoviles.html'") 