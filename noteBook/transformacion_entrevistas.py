import pandas as pd

def transformar_datos_servicio(data_frame_limpio):
    """
    Aplica 5 filtros y agrupaciones analíticas sobre el modelo de Entrevistas.
    Cumple con el esquema solicitado de filtrado y agregación con Pandas.
    """
    print("\n" + "="*55)
    print("📊 REQUERIMIENTO: ANALÍTICA Y TRANSFORMACIÓN DE DATOS (ENTREVISTAS)")
    print("="*55)
    
    try:
        # 1. FILTRO: Entrevistas con calificación excelente (Mayor o igual a 4)
        filtro_excelentes = data_frame_limpio[data_frame_limpio['calificacion'] >= 4]
        print(f"\n1️⃣ Filtro - Candidatos Destacados (Calificación >= 4):")
        print(f"   -> Se encontraron {len(filtro_excelentes)} entrevistas con alto desempeño.")
        
        # 2. FILTRO: Candidatos que fueron aprobados (Aprobado == True)
        filtro_aprobados = data_frame_limpio[data_frame_limpio['Aprobado'] == True]
        print(f"\n2️⃣ Filtro - Personal Aprobado para Contratación:")
        print(f"   -> {len(filbro_aprobados) if 'filbro_aprobados' in locals() else len(filtro_aprobados)} candidatos listos para pasar a la siguiente fase.")
        
        # 3. FILTRO COMBINADO: Calificación baja (< 3) pero aprobados (Alerta de coherencia)
        filtro_alertas = data_frame_limpio[(data_frame_limpio['calificacion'] < 3) & (data_frame_limpio['Aprobado'] == True)]
        print(f"\n3️⃣ Filtro - Casos Especiales / Alertas (Calificación < 3 y Aprobado):")
        print(f"   -> Se detectaron {len(filtro_alertas)} casos que requieren revisión de auditoría.")
        
        # 4. AGRUPACIÓN: Rendimiento por Entrevistador (Promedio de calificaciones otorgadas)
        print(f"\n4️⃣ Agrupación - Promedio de Calificación por Entrevistador:")
        agrupacion_entrevistador = data_frame_limpio.groupby('entrevistador')['calificacion'].mean().reset_index()
        print(agrupacion_entrevistador.to_string(index=False))
        
        # 5. AGRUPACIÓN: Distribución de estados de aprobación según los puntajes
        print(f"\n5️⃣ Agrupación - Matriz de Calificación vs Estado de Aprobación:")
        agrupacion_estados = data_frame_limpio.groupby(['calificacion', 'Aprobado']).size().unstack(fill_value=0)
        print(agrupacion_estados)
        
        print("\n" + "="*55)
        
    except Exception as e:
        print(f"❌ Error en la transformación analítica de entrevistas: {e}")
        