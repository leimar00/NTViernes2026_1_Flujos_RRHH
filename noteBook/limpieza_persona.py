import pandas as pd

def limpiar_simulacion(data_frame):
    data_frame_limpio = data_frame.copy()

    #1. limpieza de datos de texto
    datos_texto = ["nombreCompleto", "email", "telefono", "genero", "ciudad_residencia", "fecha_de_nacimiento", "tipo_documento"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #2. convertir columnas numericas

    data_frame_limpio["id_persona"]= pd.to_numeric(data_frame_limpio["id_persona"])


    #4 eliminar valores invalidos

    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_persona"]> 0]
    
    
    # validar que si sean numeros
    solo_numeros = data_frame_limpio["telefono"].str.isdigit()
    data_frame_limpio = data_frame_limpio[solo_numeros]


    # Controlar valores esperados
    valores_esperados_tipo_documento = ["CC", "CE", "PPT"]
    data_frame_limpio["tipo_documento"] = data_frame_limpio["tipo_documento"].where(
        data_frame_limpio["tipo_documento"].isin(valores_esperados_tipo_documento),
        pd.NA
    )

    valores_esperados_ciudad = ["Medellin", "Envigado", "Barbosa", "Copacabana", "Sabaneta", "Itagui", "La Estrella", "Bello"]
    data_frame_limpio["ciudad_residencia"] = data_frame_limpio["ciudad_residencia"].where(
        data_frame_limpio["ciudad_residencia"].isin(valores_esperados_ciudad),
        pd.NA
    )

    valores_esperados_genero = ["Masculino", "Femenino", "No binario", "Otro"]
    data_frame_limpio["genero"] = data_frame_limpio["genero"].where(
        data_frame_limpio["genero"].isin(valores_esperados_genero),
        pd.NA
    )

    # limpieza de fechas
    data_frame_limpio["fecha_de_nacimiento"] = pd.to_datetime(data_frame_limpio["fecha_de_nacimiento"])

    # reemplazar fechas nulas por un indicativo de error
    indicativo = pd.to_datetime("1000-01-01")
    data_frame_limpio["fecha_de_nacimiento"] = data_frame_limpio["fecha_de_nacimiento"].fillna(indicativo)

    #5 eliminar duplicados

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    #6 validar el largo del telefono

    largo_esperado = 10

    es_valido = data_frame_limpio["telefono"].str.len() == largo_esperado

    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].mask(
    ~es_valido,                           # El símbolo ~ invierte la condición (los que NO miden 10)
    data_frame_limpio["telefono"] + "Err"   # El nuevo valor: el original + un Err
    )

    #3. eliminar filas con nulos en columnas obligatorias

    columnas_obligatorias = ["nombreCompleto", "email", "telefono", "id_persona", "fecha_de_nacimiento", "tipo_documento"]

    data_frame_limpio = data_frame_limpio.dropna(subset= columnas_obligatorias)

    return data_frame_limpio