import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Parte 1: Arreglo NumPy de productividad semanal ---
productividad = np.array([75, 80, 90, 85, 70])
promedio = np.mean(productividad)
maximo = np.max(productividad)

print("Productividad semanal:", productividad)
print(f"Promedio de productividad: {promedio}")
print(f"Valor máximo de productividad: {maximo}")


# --- Parte 2: Leer archivo empleados.csv ---
ruta = r"C:\Users\josue\OneDrive\Escritorio\Escuela\8° Semestre\Prog. Log. y Func\empleados.csv"
df = pd.read_csv(ruta)
print("\nArchivo 'empleados.csv' leído correctamente.")

# Mostrar empleados del departamento Ventas
ventas = df[df["Departamento"] == "Ventas"]
print("\nEmpleados del departamento de Ventas:")
print(ventas["Nombre"])

# --- Parte 3: Agregar columna 'Bono' (10% del salario) ---
df["Bono"] = df["Salario"] * 0.10
print("\nColumna 'Bono' agregada con éxito.")

# --- Parte 4: Gráfica de salarios ---
plt.figure(figsize=(12, 6))
plt.bar(df["Nombre"], df["Salario"], color='skyblue')
plt.title("Salario de Empleados")
plt.xlabel("Nombre")
plt.ylabel("Salario")
plt.xticks(rotation=90)  # Evita nombres encimados
plt.tight_layout()
plt.show()
