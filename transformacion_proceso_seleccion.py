import pandas as pd

def transformar_procesos(data_frame_limpio):

    # Transformacion 1 (procesos por fecha)
    agrupacion1 = data_frame_limpio.groupby("fecha")["idProceso"].count().reset_index(name="conteo")

    # Transformacion 2 (procesos con puntaje aprobatorio)
    filtro2 = data_frame_limpio.query("puntajePruebas >= 60")
    agrupacion2 = filtro2.groupby("estadoProceso")["idProceso"].count().reset_index(name="conteo")

    # Transformacion 3 (estado vs fecha para mapa de calor)
    filtro3 = data_frame_limpio.query("puntajePruebas >= 0")
    agrupacion3 = filtro3.groupby(["estadoProceso", "fecha"])["idProceso"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3
    }

    return agrupacion_resumen