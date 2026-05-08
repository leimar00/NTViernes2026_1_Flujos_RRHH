import pandas as pd

# ZONA DE IMPORTACIÓN (Carpetas y Archivos)
from utils.simulacionDatosEntrevista import generarEntrevista 
from noteBook.Limpieza_Entrevista import limpiar_entrevistas
# Importamos las funciones de descripción (asumiendo que las guardaste en este archivo)
from noteBook.Descripcion_Entrevista import (
    describir_estructura_entrevistas,
    describir_estadisticas_entrevistas,
    describir_categoricas_entrevistas,
)

# 1. GENERACIÓN: Llamas a la simulación
# Te sugiero subir a 50 o 100 para que las estadísticas se vean más interesantes
datos_sucios = generarEntrevista(50)

# 2. ESTRUCTURACIÓN: Convertir a DataFrame
df_sucio = pd.DataFrame(datos_sucios)

# 3. TRANSFORMACIÓN: Aplicar la limpieza de los 8 pasos
df_limpio = limpiar_entrevistas(df_sucio)

# 4. ANÁLISIS: Aplicar la lógica del profesor para describir los resultados
print("\n" + "="*50)
print("REPORTE FINAL DE ENTREVISTAS - CESDE 2026")
print("="*50)

describir_estructura_entrevistas(df_limpio)
describir_estadisticas_entrevistas(df_limpio)
describir_categoricas_entrevistas(df_limpio)