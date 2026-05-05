import pandas as pd

def limpiar_simulacion(data_frame):
    data_frame_limpio = data_frame.copy()

    #1. limpieza de datos de texto
    datos_texto = ["nombreCompleto", "email", "telefono"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #2. convertir columnas numericas

    data_frame_limpio["id_persona"]= pd.to_numeric(data_frame_limpio["id_persona"])

    #3. eliminar filas con nulos en columnas obligatorias

    columnas_obligatorias = ["nombreCompleto", "email", "telefono", "id_persona"]

    data_frame_limpio = data_frame_limpio.dropna(subset= columnas_obligatorias)

    #4 eliminar valores invalidos

    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_persona"]> 0]
    
    
    solo_numeros = data_frame_limpio["telefono"].str.isdigit()
    data_frame_limpio = data_frame_limpio[solo_numeros]

    #5 eliminar duplicados

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    #6 validar el largo del telefono

    largo_esperado = 10

    es_valido = data_frame_limpio["telefono"].str.len() == largo_esperado

    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].mask(
    ~es_valido,                           # El símbolo ~ invierte la condición (los que NO miden 10)
    data_frame_limpio["telefono"] + "Err"   # El nuevo valor: el original + un Err
    )

    return data_frame_limpio