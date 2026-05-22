import pandas as pd

def transformar_datos_vacante(data_frame_limpio):
    resultados = {}

    # ==========================================================
    # FILTRO 1: Vacantes abiertass
    # ==========================================================
    filtro1 = data_frame_limpio[data_frame_limpio["estadoVacante"] == "ABIERTA"]
    agrupacion1 = filtro1.groupby("fecha_vacante")["id"].count().reset_index(name="cantidad_vacantes")
    resultados["vacantes_abiertas"] = agrupacion1

    # ==========================================================
    # FILTRO 2: Vacantes con mayor presupuesto
    # ==========================================================
    filtro2 = data_frame_limpio[data_frame_limpio["presupuestoSalario"] > 2800]
    agrupacion2 = filtro2.groupby("tituloCargo")["presupuestoSalario"].mean().reset_index(name="promedio_salario")
    resultados["vacantes_alta_demanda"] = agrupacion2

    # ==========================================================
    # FILTRO 3: Posiciones específicas (Developer)
    # ==========================================================
    filtro3 = data_frame_limpio[data_frame_limpio["titulo_log"].str.contains("Developer", na=False)]
    agrupacion3 = filtro3.groupby("tituloCargo")["id"].count().reset_index(name="cantidad")
    resultados["posicion_developer"] = agrupacion3

    # ==========================================================
    # FILTRO 4: Fechas recientes (últimos 30 días)
    # ==========================================================
    fecha_max = data_frame_limpio["fecha_vacante"].max()
    filtro4 = data_frame_limpio[data_frame_limpio["fecha_vacante"] >= fecha_max - pd.Timedelta(days=30)]
    agrupacion4 = filtro4.groupby("fecha_vacante")["presupuestoSalario"].sum().reset_index(name="total_presupuesto")
    resultados["ultimos_30_dias"] = agrupacion4

    # ==========================================================
    # FILTRO 5: Departamentos con más vacantes
    # ==========================================================
    conteo = data_frame_limpio["tituloCargo"].value_counts()
    departamentos_activos = conteo[conteo > 1].index
    filtro5 = data_frame_limpio[data_frame_limpio["tituloCargo"].isin(departamentos_activos)]
    agrupacion5 = filtro5.groupby("tituloCargo")["id"].count().reset_index(name="cantidad_vacantes")
    resultados["departamentos_activos"] = agrupacion5

    transformacion = {
        "vacantesAbiertas":      resultados.get("vacantes_abiertas"),
        "vacantesAltaDemanda":   resultados.get("vacantes_alta_demanda"),
        "posicionDeveloper":     resultados.get("posicion_developer"),
        "ultimos30Dias":         resultados.get("ultimos_30_dias"),
        "departamentosActivos":  resultados.get("departamentos_activos"),
    }

    return transformacion