import pandas as pd

def limpiar_procesos(data_frame):
    data_frame_limpio = data_frame.copy()
    
    # 1. Limpiar espacios en texto
    columnas_texto = ["estadoProceso", "observaciones"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    # 2. Definir valores esperados
    estados_validos = ["postulado", "filtrado", "en pruebas", "entrevista", "seleccionado", "rechazado"]
    data_frame_limpio["estadoProceso"] = data_frame_limpio["estadoProceso"].where(
        data_frame_limpio["estadoProceso"].isin(estados_validos),
        pd.NA
    )

    # 3. Convertir columna numérica
    data_frame_limpio["puntajePruebas"] = pd.to_numeric(data_frame_limpio["puntajePruebas"], errors="coerce")

    # 4. Convertir columna a fecha
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors="coerce")
    
    # 5. Reemplazar fechas nulas
    fecha_defecto = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_defecto)

    # 6. Eliminar filas con datos obligatorios vacíos
    columnas_obligatorias = ["idProceso", "estadoProceso", "puntajePruebas"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 7. Eliminar valores inválidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["puntajePruebas"] >= 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["puntajePruebas"] <= 100]

    # 8. Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio