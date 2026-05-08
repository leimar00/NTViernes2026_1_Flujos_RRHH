import pandas as pd

# funcion para describir la estructura general de un dataset
def describir_estructura_aspirantes(data_frame):
    print("Estructura general del dataset de Aspirantes:")
    print(f"Número de filas: {len(data_frame)}")
    print(f"Número de columnas: {len(data_frame.columns)}")
    print("\nPrimeras filas del dataset:")
    print(data_frame.head())
    print("\nÚltimas filas del dataset:")
    print(data_frame.tail())
    print("\nResumen estadístico del dataset:")
    print(data_frame.describe())
    print("\nTipos de datos:")
    print(data_frame.dtypes)
    print("\nValores nulos por columna:")
    print(data_frame.isnull().sum())

# funcion para describir estadisticas del data frame 
def estadisticas_aspirantes(data_frame):
    print("\n=== ESTADÍSTICAS DETALLADAS ===")
    print(f"Experiencia promedio: {data_frame['anos_experiencia'].mean():.2f} años")
    print(f"Experiencia mínima: {data_frame['anos_experiencia'].min()} años")
    print(f"Experiencia máxima: {data_frame['anos_experiencia'].max()} años")

# funcion para medir las columnas categoricas
def analizar_categoricas_aspirantes(data_frame):
    print("\n=== ANÁLISIS CATEGÓRICO ===")
    print("Experiencias:")
    print(data_frame['experiencias'].value_counts())
    print("\nHabilidades técnicas:")
    print(data_frame['habilidades_tecnicas'].value_counts())
    print("\nFormación académica:")
    print(data_frame['formacion_academica'].value_counts())

# funcion para describir los rangos de fechas 
def analizar_fechas_aspirantes(data_frame):
    print("\n=== ANÁLISIS DE FECHAS ===")
    print(f"Fecha de solicitud más antigua: {data_frame['fecha_solicitud'].min()}")
    print(f"Fecha de solicitud más reciente: {data_frame['fecha_solicitud'].max()}")
