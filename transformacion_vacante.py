import pandas as pd

def transformar_datos_vacante(data_frame_limpio):
    resultados = {}

    # ==========================================================
    # FILTRO 1: Vacantes por estado específico (ej. abierta)
    # ==========================================================
    filtro1 = data_frame_limpio.query("estado == 'abierta'")
    agrupacion1 = filtro1.groupby("fecha_publicacion")["id"].count().reset_index(name="cantidad_vacantes")
    resultados["vacantes_abiertas"] = agrupacion1

    # ==========================================================
    # FILTRO 2: Vacantes con muchos aspirantes
    # ==========================================================
    filtro2 = data_frame_limpio.query("cantidad_aspirantes > 10")
    agrupacion2 = filtro2.groupby("departamento")["cantidad_aspirantes"].mean().reset_index(name="promedio_aspirantes")
    resultados["vacantes_alta_demanda"] = agrupacion2

    # ==========================================================
    # FILTRO 3: Posiciones específicas
    # ==========================================================
    filtro3 = data_frame_limpio.query("posicion == 'Developer'")
    agrupacion3 = filtro3.groupby("departamento")["id"].count().reset_index(name="cantidad")
    resultados["posicion_developer"] = agrupacion3

    # ==========================================================
    # FILTRO 4: Fechas recientes (últimos 30 días)
    # ==========================================================
    fecha_max = data_frame_limpio["fecha_publicacion"].max()
    filtro4 = data_frame_limpio[data_frame_limpio["fecha_publicacion"] >= fecha_max - pd.Timedelta(days=30)]
    agrupacion4 = filtro4.groupby("fecha_publicacion")["cantidad_aspirantes"].sum().reset_index(name="total_aspirantes")
    resultados["ultimos_30_dias"] = agrupacion4

    # ==========================================================
    # FILTRO 5: Departamentos con más vacantes
    # ==========================================================
    conteo = data_frame_limpio["departamento"].value_counts()
    departamentos_activos = conteo[conteo > 3].index
    filtro5 = data_frame_limpio[data_frame_limpio["departamento"].isin(departamentos_activos)]
    agrupacion5 = filtro5.groupby("departamento")["id"].count().reset_index(name="cantidad_vacantes")
    resultados["departamentos_activos"] = agrupacion5


    # Además devolver un diccionario con las transformaciones principales
    transformacion = {
        "vacantesAbiertas": resultados.get("vacantes_abiertas"),
        "vacantesAltaDemanda": resultados.get("vacantes_alta_demanda"),
        "posicionDeveloper": resultados.get("posicion_developer"),
        "ultimos30Dias": resultados.get("ultimos_30_dias"),
        "departamentosActivos": resultados.get("departamentos_activos"),
    }

    return transformacion
