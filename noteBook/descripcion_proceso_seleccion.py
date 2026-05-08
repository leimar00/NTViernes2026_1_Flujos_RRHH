import pandas as pd

def describir_estructura(data_frame_limpio): # Función para describir la estructura general del DataFrame limpio
    print("**** ESTRUCTURA GENERAL ****") # Imprime un encabezado para la sección de descripción general
    print(f"Número de filas: {data_frame_limpio.shape[0]}") # Imprime el número de filas en el DataFrame limpio
    print(f"Número de columnas: {data_frame_limpio.shape[1]}") # Imprime el número de columnas en el DataFrame limpio
    print(f"Columnas disponibles: {list(data_frame_limpio.columns)}") # Imprime la lista de columnas disponibles en el DataFrame limpio


def describir_estadisticas(data_frame_limpio): # Función para describir estadísticas básicas de las columnas numéricas en el DataFrame limpio
    print("\n**** ESTADÍSTICAS ****") # Imprime un encabezado para la sección de estadísticas
    print(f"{data_frame_limpio[['idProceso', 'puntajePruebas']].describe()}") # Imprime estadísticas descriptivas para las columnas 'idProceso' y 'puntajePruebas' en el DataFrame limpio


def describir_categoricas(data_frame_limpio):
    print("\n**** FRECUENCIAS CATEGÓRICAS ****")
    print("Estados del Proceso:")
    print(f"{data_frame_limpio['estadoProceso'].value_counts()}")
    print()
    print("Observaciones:")
    print(f"{data_frame_limpio['observaciones'].value_counts()}")


def describir_fechas(data_frame_limpio):
    print("\n**** RANGOS DE FECHAS ****")
    print(f"Fecha mínima: {data_frame_limpio['fecha'].min()}")
    print(f"Fecha máxima: {data_frame_limpio['fecha'].max()}")