import pandas as pd
from datetime import datetime


def transformar_datos_aspirantes(data_frame_limpio):
    
    df = data_frame_limpio.copy()

    resultados = {}

    # FILTRO 1: Aspirantes con habilidad 'python' -> distribución por formación
    filtro1 = df[df["habilidades_tecnicas"] == "python"]
    agrupacion1 = (
        filtro1.groupby("formacion_academica")["id"]
        .count()
        .reset_index(name="cuenta_python_por_formacion")
        .sort_values("cuenta_python_por_formacion", ascending=False)
    )
    resultados["python_por_formacion"] = agrupacion1

    # FILTRO 2: Aspirantes con >=5 años de experiencia -> conteo por experiencia declarada
    filtro2 = df[df["anos_experiencia"] >= 5]
    agrupacion2 = (
        filtro2.groupby("experiencias")["id"]
        .count()
        .reset_index(name="cuenta_experiencia_5mas")
        .sort_values("cuenta_experiencia_5mas", ascending=False)
    )
    resultados["experiencia_5mas_por_tipo"] = agrupacion2

    # FILTRO 3: Formacion 'bootcamp full stack' -> distribución por habilidades
    filtro3 = df[df["formacion_academica"] == "bootcamp full stack"]
    agrupacion3 = (
        filtro3.groupby("habilidades_tecnicas")["id"]
        .count()
        .reset_index(name="cuenta_bootcamp_por_habilidad")
        .sort_values("cuenta_bootcamp_por_habilidad", ascending=False)
    )
    resultados["bootcamp_por_habilidad"] = agrupacion3

    # FILTRO 4: Solicitudes recientes (últimos 30 días) -> tendencia por fecha
    try:
        fecha_max = pd.to_datetime(df["fecha_solicitud"]).max()
    except Exception:
        fecha_max = pd.to_datetime(datetime.now())

    filtro4 = df[pd.to_datetime(df["fecha_solicitud"]) >= fecha_max - pd.Timedelta(days=30)]
    # normalizar a columna fecha para agrupar
    agrupacion4 = (
        filtro4.assign(fecha=pd.to_datetime(filtro4["fecha_solicitud"]).dt.date)
        .groupby("fecha")["id"]
        .count()
        .reset_index(name="cantidad_solicitudes_30d")
        .sort_values("fecha")
    )
    resultados["ultimas_30_dias_por_fecha"] = agrupacion4

    # FILTRO 5: Top habilidades técnicas (conteo y acumulado)
    agrupacion5 = (
        df.groupby("habilidades_tecnicas")["id"]
        .count()
        .reset_index(name="cuenta_por_habilidad")
        .sort_values("cuenta_por_habilidad", ascending=False)
        .assign(acumulado=lambda x: x["cuenta_por_habilidad"].cumsum())
    )
    resultados["habilidad_cuenta_acumulado"] = agrupacion5

    return resultados
