import pandas as pd


def limpiar_entrevistas(df):
    # 1. Copia y limpieza básica de strings
    df_limpio = df.copy()

    #limpieza de string para espacios vacios

    datos_texto = ["entrevistador", "comentarios"]
    for columna in datos_texto:
        df_limpio[columna] = df_limpio[columna].astype(str).str.strip()


    # 2. Listas de validación (Dominio del profesor)

    nombres_validos = ["leimar_henao", "julian_mendez", "Alma_Marcela_gozo", "Homero_sipson"]
    comentarios_validos = [
        "tiene conociemiento sobre todo lo requerido", 
        "tiene conocimientos basicos en PY y necesita reforzar en React", 
        "no cumple con los requisitos minimos para developer junior"
    ]

    # 3. Validar pertenencia (Si no está en la lista, fuera)
    df_limpio["entrevistador"] = df_limpio["entrevistador"].where(df_limpio["entrevistador"].isin(nombres_validos,), pd.NA)
    df_limpio["comentarios"] = df_limpio["comentarios"].where(df_limpio["comentarios"].isin(comentarios_validos), pd.NA)

    # 4. Convertir Números
    df_limpio["id_entrevistador"] = pd.to_numeric(df_limpio["id_entrevistador"], errors='coerce')
    df_limpio["calificacion"] = pd.to_numeric(df_limpio["calificacion"], errors='coerce')


# 5. TRATAMIENTO DE FECHAS (Lógica Estricta)
    
    # Paso A: Forzamos el formato EXACTO (Día/Mes/Año con 4 dígitos)
    # Al poner format='%d/%m/%Y', cualquier cosa que sea solo "15/05" fallará
    # y se convertirá en NaT automáticamente.
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"], format='%d/%m/%Y', errors='coerce')
    
    # Paso B: (Opcional pero recomendado) Por si se coló algún año loco
    df_limpio.loc[df_limpio["fecha"].dt.year < 2000, "fecha"] = pd.NaT
    
    # Paso C: Ahora sí, todo lo que falló (incluyendo tus fechas de 2 dígitos)
    # se convierte en la fecha general.
    df_limpio["fecha"] = df_limpio["fecha"].fillna(pd.Timestamp(2026, 1, 1))


    # 6. Limpiar Booleano
    df_limpio["Aprobado"] = df_limpio["Aprobado"].astype(str).str.lower().map({"true": True, "false": False})
    df_limpio["Aprobado"] = df_limpio["Aprobado"].fillna(False)

    # 7. Eliminar registros sin ID o sin Entrevistador (Datos obligatorios)
    df_limpio = df_limpio.dropna(subset=["id_entrevistador", "entrevistador"])

    # 8. Reglas de Negocio y Duplicados
    df_limpio = df_limpio[df_limpio["id_entrevistador"] > 0]
    df_limpio = df_limpio[(df_limpio["calificacion"] >= 1) & (df_limpio["calificacion"] <= 5)]
    df_limpio = df_limpio.drop_duplicates()

    return df_limpio