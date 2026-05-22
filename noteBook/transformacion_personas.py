import pandas as pd

def transformar_datos_persona(data_frame_limpio):

    # ── FILTRO 1 ──────────────────────────────────────────────────
    # Residentes en Medellín    
    filtro1 = data_frame_limpio.query("ciudad_residencia == 'Medellin'")

    # Agrupación 1a: conteo por teléfono
    agrupacion1a = (
        filtro1
        .groupby("telefono")["id_persona"]
        .count()
        .reset_index(name="cuenta_medellin_telefono")
    )
    # Columnas resultado: telefono | cuenta_medellin_telefono

    # Agrupación 1b: conteo por género
    agrupacion1b = (
        filtro1
        .groupby("genero")["id_persona"]
        .count()
        .reset_index(name="cuenta_medellin_genero")
        .sort_values("cuenta_medellin_genero", ascending=False)
    )
    # Columnas resultado: genero | cuenta_medellin_genero

    # ── FILTRO 2 ──────────────────────────────────────────────────
    # Solo género Femenino → distribución por ciudad de residencia
    filtro2 = data_frame_limpio.query("genero == 'Femenino'")

    agrupacion2 = (
        filtro2
        .groupby("ciudad_residencia")["id_persona"]
        .count()
        .reset_index(name="cuenta_femenino_ciudad")
        .sort_values("cuenta_femenino_ciudad", ascending=False)
    )
    # Columnas resultado: ciudad_residencia | cuenta_femenino_ciudad

    # ── FILTRO 3 ──────────────────────────────────────────────────
    # Mayores de 35 años → conteo por tipo de documento
    filtro3 = data_frame_limpio.query("edad > 35")

    agrupacion3 = (
        filtro3
        .groupby("tipo_documento")["id_persona"]
        .count()
        .reset_index(name="cuenta_mayores35")
        .sort_values("cuenta_mayores35", ascending=False)
    )
    # Columnas resultado: tipo_documento | cuenta_mayores35

    # ── FILTRO 4 ──────────────────────────────────────────────────
    # Portadores de CC o TI → conteo por ciudad de residencia
    filtro4 = data_frame_limpio.query("tipo_documento in ['CC', 'TI']")

    agrupacion4 = (
        filtro4
        .groupby("ciudad_residencia")["id_persona"]
        .count()
        .reset_index(name="cuenta_cc_ti_ciudad")
        .sort_values("cuenta_cc_ti_ciudad", ascending=False)
    )
    # Columnas resultado: ciudad_residencia | cuenta_cc_ti_ciudad

    # ── FILTRO 5 ──────────────────────────────────────────────────
    # Nacidos entre 1990 y 2000 → conteo y acumulado por rango_edad

    # CORRECCIÓN 2 → query en un solo string claro, sin concatenación implícita
    filtro5 = data_frame_limpio.query(
        "fecha_de_nacimiento >= '1990-01-01' and fecha_de_nacimiento <= '2000-12-31'"
    )

    agrupacion5 = (
        filtro5
        .groupby("rango_edad", observed=True)["id_persona"]
        .count()
        .reset_index(name="cuenta_decada90")
    )

    # CORRECCIÓN 3 → .assign() en lugar de asignación directa
    # evita SettingWithCopyWarning y es más seguro en todas las versiones de pandas
    agrupacion5 = agrupacion5.assign(
        acumulado=agrupacion5["cuenta_decada90"].cumsum()
    )
    # Columnas resultado: rango_edad | cuenta_decada90 | acumulado

    # ── RETORNO ───────────────────────────────────────────────────
    # CORRECCIÓN 4 → nomenclatura uniforme en snake_case
    transformacion = {
        "medellin_por_telefono"   : agrupacion1a,
        "medellin_por_genero"     : agrupacion1b,
        "femenino_por_ciudad"     : agrupacion2,
        "mayores_35_por_doc"      : agrupacion3,
        "cc_ti_por_ciudad"        : agrupacion4,
        "decada_90_acumulado"     : agrupacion5,
    }

    return transformacion