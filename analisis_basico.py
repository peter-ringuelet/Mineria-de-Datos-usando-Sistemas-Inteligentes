import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo para las gráficas
plt.style.use('seaborn')
sns.set_palette("husl")

# Ruta de los datos
DATOS_DIR = 'C:/Users/Peter/Desktop/all/Facu/Mineria De Datos Usando Sistemas Inteligentes/Datos/'

# Cargar el dataset
print("Cargando datos...")
df = pd.read_csv(DATOS_DIR + 'automobile.csv')

# 1. Información general del dataset
print("\n=== Información General del Dataset ===")
print(df.info())

# 2. Estadísticas descriptivas
print("\n=== Estadísticas Descriptivas ===")
print(df.describe())

# 3. Análisis de valores faltantes
print("\n=== Análisis de Valores Faltantes ===")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# 4. Visualizaciones

# a. Distribución de precios
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Price', bins=30, kde=True)
plt.title('Distribución de Precios')
plt.savefig('distribucion_precios.png')
plt.close()

# b. Relación entre precio y potencia
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Horsepower', y='Price')
plt.title('Relación entre Precio y Potencia')
plt.savefig('precio_vs_potencia.png')
plt.close()

# c. Precios por marca
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Make', y='Price')
plt.xticks(rotation=45)
plt.title('Distribución de Precios por Marca')
plt.tight_layout()
plt.savefig('precios_por_marca.png')
plt.close()

# d. Matriz de correlación para variables numéricas
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.tight_layout()
plt.savefig('matriz_correlacion.png')
plt.close()

# 5. Análisis de variables categóricas
print("\n=== Análisis de Variables Categóricas ===")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nDistribución de {col}:")
    print(df[col].value_counts())

# 6. Correlaciones más fuertes
print("\n=== Correlaciones más Fuertes ===")
correlations = correlation_matrix.unstack()
sorted_correlations = correlations.sort_values(key=abs, ascending=False)
# Eliminar autocorrelaciones y duplicados
sorted_correlations = sorted_correlations[sorted_correlations != 1.0]
sorted_correlations = sorted_correlations[~sorted_correlations.index.duplicated()]
print("Top 10 correlaciones más fuertes:")
print(sorted_correlations.head(10))

print("\nAnálisis completado. Se han generado las siguientes visualizaciones:")
print("1. distribucion_precios.png")
print("2. precio_vs_potencia.png")
print("3. precios_por_marca.png")
print("4. matriz_correlacion.png") 