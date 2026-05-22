import pandas as pd




# ──────────────────────────────────────────────
# HU22 — Descripción exploratoria tabla Vacante
# ──────────────────────────────────────────────

def describir_estructura(df):
    print("**** Estructura general ****")
    print(f"Numero de filas:      {df.shape[0]}")
    print(f"Numero de columnas:   {df.shape[1]}")
    print(f"Columnas disponibles: {list(df.columns)}")


def describir_estadisticas(df):
    print("**** ESTADISTICAS ****")
    print(df[["id", "presupuestoSalario"]].describe())


def describir_categoricas(df):
    print("*** Frecuencias categoricas ***")
    print("Títulos ofrecidos:")
    print(df["titulo_log"].value_counts().to_string())
    print("\nDepartamentos:")
    print(df["tituloCargo"].value_counts().to_string())
    print("\nEstado de vacantes:")
    print(df["estadoVacante"].value_counts().to_string())


def describir_fechas(df):
    print("*** RANGOS DE FECHA ***")
    print(f"Fecha mínima: {df['fecha_vacante'].min()}")
    print(f"Fecha máxima: {df['fecha_vacante'].max()}")


def describir_todo(df):
    describir_estructura(df)
    print()
    describir_estadisticas(df)
    print()
    describir_categoricas(df)
    print()
    describir_fechas(df)


# ── Ejecución ──
if __name__ == "__main__":
    from utils.simulacion_HU23 import generar_vacantes
    from simulacion_HU21 import limpiar_vacantes

    vacantes = generar_vacantes(10)
    df_crudo = pd.DataFrame(vacantes)
    df_limpio = limpiar_vacantes(df_crudo)

    print(">>> Descripción del dataset limpio:\n")
    describir_todo(df_limpio)