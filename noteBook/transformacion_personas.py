import pandas as pd

def transformar_datos_persona(data_frame_limpio):

    filtro0 = data_frame_limpio.query("ciudad_residencia == 'Medellin'")
    agrupacion0 = filtro0.groupby("telefono")["id"].count().reset_index(name="cuenta_medellin")

    filtro1 = data_frame_limpio.query("ciudad_residencia == 'Medellin'")
    agrupacion1 = (
        filtro1.groupby("genero")["id"].count().reset_index(name="cuenta_medellin").sort_values("cuenta_medellin", ascending=False)
    )
    # Columnas resultado: genero | cuenta_medellin
 
    # ── FILTRO 2 ──────────────────────────────────────────────────
    # Solo género Femenino → distribución por ciudad de residencia
    filtro2 = data_frame_limpio.query("genero == 'Femenino'")
 
    agrupacion2 = (
        filtro2.groupby("ciudad_residencia")["id"].count().reset_index(name="cuenta_femenino_ciudad").sort_values("cuenta_femenino_ciudad", ascending=False)
    )
    # Columnas resultado: ciudad_residencia | cuenta_femenino_ciudad
 
    # ── FILTRO 3 ──────────────────────────────────────────────────
    # Mayores de 35 años → conteo por tipo de documento
    filtro3 = data_frame_limpio.query("edad > 35")
 
    agrupacion3 = (
        filtro3.groupby("tipo_documento")["id"].count().reset_index(name="cuenta_mayores35").sort_values("cuenta_mayores35", ascending=False)
    )
    # Columnas resultado: tipo_documento | cuenta_mayores35
 
    # ── FILTRO 4 ──────────────────────────────────────────────────
    # Portadores de CC o TI → conteo por ciudad de residencia
    filtro4 = data_frame_limpio.query("tipo_documento in ['CC', 'TI']")
 
    agrupacion4 = (
        filtro4.groupby("ciudad_residencia")["id"].count().reset_index(name="cuenta_cc_ti_ciudad").sort_values("cuenta_cc_ti_ciudad", ascending=False)
    )
    # Columnas resultado: ciudad_residencia | cuenta_cc_ti_ciudad
 
    # ── FILTRO 5 ──────────────────────────────────────────────────
    # Nacidos entre 1990 y 2000 → conteo y acumulado por rango_edad
    filtro5 = data_frame_limpio.query("fecha_de_nacimiento >= '1990-01-01' and ""fecha_de_nacimiento <= '2000-12-31'")
 
    agrupacion5 = (
        filtro5.groupby("rango_edad", observed=True)["id"].count().reset_index(name="cuenta_decada90")
    )
    # Columna extra: total acumulado (para gráfico de línea)
    agrupacion5["acumulado"] = agrupacion5["cuenta_decada90"].cumsum()
    # Columnas resultado: rango_edad | cuenta_decada90 | acumulado
 

    transformacion = {
        "cuentaMedellinTelefonos" : agrupacion0,
        "cuentaMedellinGenero" : agrupacion1,
        "generoFemeninoPorCiudad" : agrupacion2,
        "mayoresDe35CuentaDNI" : agrupacion3,
        "CCoTIPorCiudad" : agrupacion4,
        "cuenta_Decada90" : agrupacion5
    }

    return transformacion