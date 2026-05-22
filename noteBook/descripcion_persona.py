import pandas as pd

def describir_estructura(data_frame_limpio): 
    print("**** Estructura general *****")
    print(f"Numero de filas: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo: {data_frame_limpio.dtypes}")

def describir_estadisticas(data_frame_limpio):
    print("\n****** Estadisticas *******")
    print(f"{data_frame_limpio[["id"]].describe()}")

    # describir las fechas
    print("*** DESCRIPCION DE FECHAS ***")
    print(f"{data_frame_limpio["fecha_de_nacimiento"].min()}")
    print(f"{data_frame_limpio["fecha_de_nacimiento"].max()}")