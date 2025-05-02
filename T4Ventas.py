# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creación de arreglos con numpy
# Arreglo de ventas por semana
ventas_semana = np.array([150, 200, 170, 220, 300, 250,
190])
print("Ventas por semana:", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:",
np.mean(ventas_semana))
print("Ventas máxima:",
np.max(ventas_semana))
print("Ventas mínima:",
np.min(ventas_semana))

# Lectura de archivos CSV con pandas
datos_ventas = pd.read_csv(r"C:\Tec\Octavo\plyf\Tema1\Tema 4\ventas.csv", encoding='utf-8')
print("\nDatos de ventas:\n", datos_ventas)

# Visualización de datos con matplotlib
# Gráfica de barras de Unidades Vendidas por Producto
plt.bar(datos_ventas['Producto'], datos_ventas['Unidades Vendidas'], color='skyblue')
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.show()
