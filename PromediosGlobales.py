import pandas as pd

df = pd.read_csv("Calificaciones globales.csv", encoding="latin1")

# Limpiar espacios en nombres de columnas
df.columns = df.columns.str.strip()

print(df.head)

print(df.columns)

df["Promedio"] = (df["Parcial 1"] + df["Parcial 2"] + df["Parcial 3"]) / 3
df["Promedio"] = df["Promedio"].round(1)
print(df[["Alumno", "Promedio"]])



# Promedio grupal
print("\nEstadísticas generales:")
print("Promedio del grupo:")
print(df[["Parcial 1", "Parcial 2", "Parcial 3"]].mean())

# Mediana grupal
print("Mediana del grupo:", df["Promedio"].median())

# Frecuencia
print("Frecuencia: ", df["Promedio"].value_counts())

# Rango
rango = df["Promedio"].max() - df["Promedio"].min()
print("Rango = Valor máximo: ", df["Promedio"].max(), "-", "Valor mínimo: ", df["Promedio"].min() , "=", round(rango, 1))
