import pandas as pd

def limpiar_datos_aspirantes(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #Procesando los textos del DF SUCIO

    #1. Limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].astype("string").str.strip().str.lower()
    data_frame_limpio["experiencias"]=data_frame_limpio["experiencias"].astype("string").str.strip().str.lower()
    data_frame_limpio["habilidades_tecnicas"]=data_frame_limpio["habilidades_tecnicas"].astype("string").str.strip().str.lower()
    data_frame_limpio["formacion_academica"]=data_frame_limpio["formacion_academica"].astype("string").str.strip().str.lower()

    #2. Limpiando los textos para controlar valores inesperados
    valores_esperados_experiencias=["desarrollo web","análisis de datos","diseño gráfico","devops","qa testing"]
    data_frame_limpio["experiencias"]=data_frame_limpio["experiencias"].where(
        data_frame_limpio["experiencias"].isin(valores_esperados_experiencias),
        pd.NA
    )

    valores_esperados_habilidades=["python","javascript","sql","react","java","c++","docker","aws"]
    data_frame_limpio["habilidades_tecnicas"]=data_frame_limpio["habilidades_tecnicas"].where(
        data_frame_limpio["habilidades_tecnicas"].isin(valores_esperados_habilidades),
        pd.NA
    )

    valores_esperados_formacion=["licenciatura en informática","bootcamp full stack","técnico en programación","ingeniería de sistemas"]
    data_frame_limpio["formacion_academica"]=data_frame_limpio["formacion_academica"].where(
        data_frame_limpio["formacion_academica"].isin(valores_esperados_formacion),
        pd.NA
    )

    #Limpieza de datos numericos

    #1. VERIFICAR QUE LOS NUMEROS SI SEAN NUMEROS
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["anos_experiencia"]=pd.to_numeric(data_frame_limpio["anos_experiencia"])

    #2. Verifiquemos los valores numericos esperados
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["anos_experiencia"]>=0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["anos_experiencia"]<=15]

    #Limpieza de FECHAS
    #1. Verificar que el campo si es una fecha
    data_frame_limpio["fecha_solicitud"]=pd.to_datetime(data_frame_limpio["fecha_solicitud"])

    #2. Reemplazar fechas que no llegan por una fecha por defecto
    fecha_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha_solicitud"]=data_frame_limpio["fecha_solicitud"].fillna(fecha_default)

    #NOVEDADES de datos vacios
    columnas_obligatorias=["id","nombre","experiencias","habilidades_tecnicas","formacion_academica"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio
