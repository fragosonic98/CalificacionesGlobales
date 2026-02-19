# CalificacionesGlobales
Este programa en Python permite importar un archivo CSV con calificaciones de alumnos y calcular estadísticas básicas
  ✅ Promedio individual por alumno

  📈 Promedio general del grupo
  
  📊 Mediana
  
  📋 Frecuencia de promedios
  
  📏 Rango (máximo - mínimo)

El proyecto utiliza la librería pandas para el manejo y análisis de datos.

# Estructura del Archivo CSV

El archivo debe contener las siguientes columnas:

Alumno, Parcial 1, Parcial 2, Parcial 3


Ejemplo:

Juan, 8, 9, 7
Ana, 10, 9, 9
Luis, 6, 7, 8

#⚙️ Requisitos

Python 3.x

pandas

Instalación de pandas:

pip install pandas

#📊 Funcionalidades

El programa realiza los siguientes cálculos:

🔹 Promedio por alumno

Calcula el promedio de los tres parciales y lo redondea a un decimal.

🔹 Promedio general del grupo

Calcula la media de cada parcial.

🔹 Mediana del grupo

Obtiene la mediana de los promedios.

🔹 Frecuencia

Muestra cuántas veces se repite cada promedio.

🔹 Rango

Calcula la diferencia entre el promedio más alto y el más bajo.
