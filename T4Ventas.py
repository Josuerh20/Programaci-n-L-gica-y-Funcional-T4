# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creación de arreglos con numpy
ventas_semana = np.array([150, 200, 170, 220, 300, 250, 190]) 
print("Ventas por semana:", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:", np.mean(ventas_semana))
print("Venta máxima:", np.max(ventas_semana))
print("Venta mínima:", np.min(ventas_semana))

# Lectura de archivo CSV con separador adecuado
datos_ventas = pd.read_csv(
    r"C:\Users\josue\OneDrive\Escritorio\Escuela\8° Semestre\Prog. Log. y Func\Ventas.csv",
    encoding='utf-8',
    sep=';'
)

# Mostrar datos originales
print("\nDatos de ventas (originales):\n", datos_ventas)

# Conversión y limpieza de la columna 'Unidades Vendidas'
datos_ventas['Unidades Vendidas'] = pd.to_numeric(
    datos_ventas['Unidades Vendidas'], errors='coerce'
).fillna(0)

# Visualización de datos con matplotlib
plt.bar(datos_ventas['Producto'], datos_ventas['Unidades Vendidas'], color='skyblue')
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.tight_layout()  # Ajusta el diseño para que no se corte el texto
plt.show()
