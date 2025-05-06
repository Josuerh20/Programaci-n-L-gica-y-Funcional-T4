
# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lectura de archivo CSV con separador adecuado
datos_ventas = pd.read_csv(
    r"C:\Users\josue\OneDrive\Escritorio\Escuela\8° Semestre\Prog. Log. y Func\Ventas.csv",
    encoding='utf-8',
    sep=';'
)

# Conversión de columnas a datos numéricos
datos_ventas['Unidades Vendidas'] = pd.to_numeric(
    datos_ventas['Unidades Vendidas'], errors='coerce'
).fillna(0)

datos_ventas['Precio Unitario'] = pd.to_numeric(
    datos_ventas['Precio Unitario'], errors='coerce'
).fillna(0)

# Agregar columna de ventas totales
datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']

# Mostrar el DataFrame con la nueva columna
print("\nDatos con Ventas Totales:\n", datos_ventas)

# Gráfica de barras con colores personalizados
colores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Puedes cambiar estos colores
plt.bar(datos_ventas['Producto'], datos_ventas['Unidades Vendidas'], color=colores)
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Gráfico de pastel con proporciones de unidades vendidas
plt.pie(
    datos_ventas['Unidades Vendidas'],
    labels=datos_ventas['Producto'],
    autopct='%1.1f%%',
    colors=colores,
    startangle=140
)
plt.title('Distribución de Unidades Vendidas')
plt.axis('equal')  # Para que sea un círculo perfecto
plt.tight_layout()
plt.show()
