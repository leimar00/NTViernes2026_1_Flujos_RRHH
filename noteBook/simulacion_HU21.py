import pandas as pd


# ──────────────────────────────────────────────
# HU21 — Limpieza de set de datos tabla Vacante
# ──────────────────────────────────────────────

def limpiar_vacantes(data_frame):
    df = data_frame.copy()

    # Limpiar espacios en blanco de columnas de texto
    columnas_texto = ["titulo_log", "tituloCargo", "estadoVacante", "abierta_cerrada_en_pausa"]
    for columna in columnas_texto:
        df[columna] = df[columna].astype("string").str.strip()

    # Validar valores permitidos en columnas de estado
    estados_validos = ["ABIERTA", "CERRADA", "EN_PAUSA"]
    df["estadoVacante"] = df["estadoVacante"].where(
        df["estadoVacante"].isin(estados_validos), pd.NA
    )
    df["abierta_cerrada_en_pausa"] = df["abierta_cerrada_en_pausa"].where(
        df["abierta_cerrada_en_pausa"].isin(estados_validos), pd.NA
    )

    # Convertir columnas numéricas (errores → NaN)
    df["id"]                 = pd.to_numeric(df["id"],                 errors="coerce")
    df["presupuestoSalario"] = pd.to_numeric(df["presupuestoSalario"], errors="coerce")

    # Convertir fecha y rellenar nulas con fecha por defecto
    df["fecha_vacante"] = pd.to_datetime(df["fecha_vacante"], errors="coerce")
    df["fecha_vacante"] = df["fecha_vacante"].fillna(pd.to_datetime("2026-01-01"))

    # Eliminar filas con campos obligatorios vacíos
    columnas_obligatorias = ["id", "titulo_log", "presupuestoSalario", "tituloCargo"]
    df = df.dropna(subset=columnas_obligatorias)

    # Eliminar valores inválidos
    df = df[df["presupuestoSalario"] > 0]
    df = df[df["id"] > 0]

    # Eliminar duplicados
    df = df.drop_duplicates()

    return df


# ── Ejecución ──
if __name__ == "__main__":
    from utils.simulacion_HU23 import generar_vacantes

    vacantes = generar_vacantes(10)
    df_crudo = pd.DataFrame(vacantes)

    print("--- DataFrame crudo ---")
    print(df_crudo.to_string())

    df_limpio = limpiar_vacantes(df_crudo)

    print("\n--- DataFrame limpio ---")
    print(df_limpio.to_string())