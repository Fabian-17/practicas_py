import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('edades.csv')

# Convertir las fechas de nacimiento en edades y agregar como una nueva columna
df['age'] = pd.Timestamp.now().year - pd.to_datetime(df['age'], format='%d/%m/%Y').dt.year

# Filtrar personas mayores de 25 años
df = df[df['age'] > 25]

# Determinar cuántas edades distintas existen y la frecuencia de cada una
contador_edades = df['age'].value_counts().sort_index(ascending=True).reset_index()
contador_edades.columns = ['edades', 'frecuencia']

# Mostrar el DataFrame final
print(contador_edades.to_string(index=False))


# Metodo basico para graficar X vs Y
plt.plot(contador_edades['edades'], contador_edades['frecuencia']) # se grafica una linea de color azul

plt.title('Gráfico de frecuencia absoluta')

plt.grid(True) 

plt.show() # Mostrar la gráfica luego de que ya se definió todos los elementos