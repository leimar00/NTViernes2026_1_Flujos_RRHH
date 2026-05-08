import pandas as pd

# 1. Función para describir la estructura general (Filas, Columnas y Nombres)
def describir_estructura_entrevistas(df_limpio):
    print("\n" + "="*30)
    print("***** ESTRUCTURA GENERAL *****")
    print("="*30)
    print(f"Número de entrevistas válidas: {df_limpio.shape[0]}")
    print(f"Número de datos por entrevista: {df_limpio.shape[1]}")
    print(f"Campos disponibles: {list(df_limpio.columns)}")

# 2. Función para describir estadísticas (Especialmente la Calificación)
def describir_estadisticas_entrevistas(df_limpio):
    print("\n" + "*"*30)
    print("***** ESTADÍSTICAS DE NOTAS *****")
    print("*"*30)
    # Usamos calificacion porque es tu dato numérico principal
    # id_entrevistador no se describe porque es un identificador, no una nota
    print(df_limpio[["calificacion"]].describe())

# 3. Función para medir las columnas categóricas (Entrevistadores y Comentarios)
def describir_categoricas_entrevistas(df_limpio):
    print("\n" + "-"*30)
    print("***** FRECUENCIAS CATEGÓRICAS *****")
    print("-"*30)
    print("--- Participación por Entrevistador ---")
    print(df_limpio["entrevistador"].value_counts())
    
    print("\n--- Tipos de Comentarios más comunes ---")
    print(df_limpio["comentarios"].value_counts())
    
    print("\n--- Conteo de Aprobados vs No Aprobados ---")
    print(df_limpio["Aprobado"].value_counts())

# 4. Función para describir los rangos de fechas (Cuándo se hicieron las entrevistas)
def describir_fechas_entrevistas(df_limpio):
    print("\n" + "#"*30)
    print("***** RANGOS DE FECHAS *****")
    print("#"*30)
    # Aquí verás si tu limpieza funcionó (si sale el 01/01/2026 como mínima)
    print(f"Primera entrevista registrada: {df_limpio['fecha'].min()}")
    print(f"Última entrevista registrada: {df_limpio['fecha'].max()}")