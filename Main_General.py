import pandas as pd

# ============================================================================
# 1. IMPORTACIÓN DE MÓDULOS
# ============================================================================

# ── Módulo Entrevistas ──
from utils.simulacionDatosEntrevista import generarEntrevista
from noteBook.Limpieza_Entrevista import limpiar_entrevistas
from noteBook.Descripcion_Entrevista import (
    describir_estructura_entrevistas, 
    describir_estadisticas_entrevistas,
    describir_categoricas_entrevistas
)
from noteBook.transformacion_entrevistas import transformar_datos_servicio

# ── Módulo Vacantes ──
from utils.simulacion_HU23 import generar_vacantes
from noteBook.simulacion_HU21 import limpiar_vacantes
from noteBook.simulacion_HU22 import (
    describir_estructura as desc_est_vac,
    describir_estadisticas as desc_estat_vac,
    describir_categoricas as desc_cat_vac,
    describir_fechas as desc_fec_vac
)
from noteBook.transformacion_vacante import transformar_datos_vacante

# ── Módulo Aspirantes ──
from utils.aspirantes_simulacion import generar_simulacion_aspirantes
from noteBook.aspirantes_limpieza import limpiar_datos_aspirantes
from noteBook.aspirantes_descripcion import (
    describir_estructura_aspirantes, 
    estadisticas_aspirantes,
    analizar_categoricas_aspirantes,
    analizar_fechas_aspirantes
)

# Importacion de transformacion de Aspirantes
from noteBook.transformacion_aspirantes import transformar_datos_aspirantes

# ── Módulo Personas ──
from utils.simulacion_Persona import generar_Personas
from noteBook.limpieza_persona import limpiar_simulacion as limpiar_personas
from noteBook.descripcion_persona import (
    describir_estructura as desc_est_per, 
    describir_estadisticas as desc_estat_per
)
# ¡IMPORTACIÓN CORREGIDA! Añadimos la transformación de personas
from noteBook.transformacion_personas import transformar_datos_persona

# ── Módulo Procesos de Selección ──
from utils.simulacion_proceso_seleccion import generar_procesos
from noteBook.limpieza_proceso_seleccion import limpiar_procesos
from noteBook.descripcion_proceso_seleccion import (
    describir_estructura as desc_est_proc, 
    describir_estadisticas as desc_estat_proc,
    describir_categoricas as desc_cat_proc,
    describir_fechas as desc_fec_proc
)

#importamos transformacion de procesos de seleccion
from noteBook.transformacion_proceso_seleccion import transformar_procesos


# ============================================================================
# ── 🛠️ SECCIÓN DE IMPORTS DE GRÁFICOS CORREGIDA (NOMBRES EXACTOS) ──
# ============================================================================
from noteBook import graficacion_entrevista as g_ent         # Archivo: noteBook/graficacion_entrevista.py
from noteBook import graficacion_vacantes as g_vac           # Archivo: noteBook/graficacion_vacantes.py
from noteBook import graficacion_aspirante as g_asp         # Archivo: noteBook/graficacion_aspirante.py
from noteBook import graficacion_personas as g_per           # Archivo: noteBook/graficacion_personas.py
from noteBook import graficacion_proceso_seleccion as g_sel  # Archivo: noteBook/graficacion_proceso_seleccion.py


# ============================================================================
# ── 📦 ADAPTADORES CONECTADOS A LAS FUNCIONES REALES ──
# ============================================================================

def integrar_graficos_entrevistas(df_limpio):
    col_estado = 'estado_entrevista' if 'estado_entrevista' in df_limpio.columns else df_limpio.columns[0]
    resumen = df_limpio.groupby(col_estado).size().reset_index(name='cantidad')
    # Usan los mismos datos, pero crean archivos diferentes (.png de barras y de torta)
    g_ent.graficar_barras_entrevistas(resumen, col_estado, 'cantidad')
    g_ent.graficar_torta_entrevistas(resumen, col_estado, 'cantidad')

def integrar_graficos_vacantes(df_limpio):
    # El script de tu compañero ya tiene su propio orquestador interno ('graficar_todo_vacantes')
    transformacion = transformar_datos_vacante(df_limpio)
    g_vac.graficar_todo_vacantes(transformacion)

def integrar_graficos_aspirantes(df_limpio):
    col_agrupar = 'genero' if 'genero' in df_limpio.columns else df_limpio.columns[0]
    resumen = df_limpio.groupby(col_agrupar).size().reset_index(name='total')
    # Llamamos a las funciones del archivo grafica_aspirantes.py
    g_asp.graficar_barras_aspirantes(resumen, col_agrupar, 'total', titulo="Aspirantes por Género")
    g_asp.graficar_torta_aspirantes(resumen, col_agrupar, 'total', titulo="Porcentaje de Aspirantes")

def integrar_graficos_personas(df_limpio):
    col_ciudad = 'ciudad_residencia' if 'ciudad_residencia' in df_limpio.columns else df_limpio.columns[0]
    resumen = df_limpio.groupby(col_ciudad).size().reset_index(name='conteo')
    # Tu compañero en grafica_personas.py las nombró a secas: graficar_barras y graficar_torta
    g_per.graficar_barras(resumen, col_ciudad, 'conteo', titulo="Personas por Ciudad")
    g_per.graficar_torta(resumen, col_ciudad, 'conteo', titulo="Distribución Geográfica de Personas")

def integrar_graficos_seleccion(df_limpio):
    col_estado = 'estadoProceso' if 'estadoProceso' in df_limpio.columns else df_limpio.columns[0]
    resumen = df_limpio.groupby(col_estado).size().reset_index(name='conteo')
    # Tu compañero en grafica_proceso_seleccion.py la nombró 'graficar_aprobados_por_estado'
    g_sel.graficar_aprobados_por_estado(resumen, columna_categorias=col_estado, columna_valores='conteo')


# ============================================================================
# 2. ORQUESTADOR DE MÓDULOS (Con impresión inteligente de transformaciones)
# ============================================================================

def ejecutar_modulo(nombre, func_sim, func_limp, funcs_desc):
    print(f"\n" + "="*55)
    print(f">>>> MÓDULO: {nombre.upper()} <<<<")
    print("="*55)
    
    try:
        datos = func_sim(50)
        df = pd.DataFrame(datos)
        df_limpio = func_limp(df)
        
        for f_desc in funcs_desc:
            # Ejecutamos la función descriptiva o analítica
            resultado = f_desc(df_limpio)
            
            # CONTROL INTELIGENTE: Si la función retorna un diccionario de DataFrames, los imprimimos de forma ordenada
            if isinstance(resultado, dict):
                print(f"\n📊 MATRICES DE TRANSFORMACIÓN ANALÍTICA ({f_desc.__name__}):")
                for clave, sub_df in resultado.items():
                    print(f"\n🔹 Sub-tabla: {clave}")
                    if isinstance(sub_df, pd.DataFrame):
                        if not sub_df.empty:
                            print(sub_df.to_string(index=False))
                        else:
                            print("   (Tabla vacía - No hay registros que cumplan las condiciones del filtro)")
                    else:
                        print(f"   {sub_df}")
            
        return len(df_limpio)
    except Exception as e:
        print(f"⚠️ Nota de Integración: {nombre} tuvo un inconveniente: {e}")
        return 0

# ============================================================================
# 3. FLUJO PRINCIPAL
# ============================================================================

def main():
    print("\n" + "#"*65)
    print("   SISTEMA INTEGRADO DE TALENTO HUMANO - CESDE 2026")
    print("   Líder Técnico de Integración: Leimar Henao Zapata")
    print("#"*65)

    registros_totales = 0

    # 1. Entrevistas (Inyectada tu función de gráficos)
    registros_totales += ejecutar_modulo("Entrevistas", generarEntrevista, limpiar_entrevistas, 
        [describir_estructura_entrevistas, describir_estadisticas_entrevistas, describir_categoricas_entrevistas, transformar_datos_servicio, integrar_graficos_entrevistas])
    
    # 2. Vacantes (Inyectado su generador masivo 'integrar_graficos_vacantes')
    registros_totales += ejecutar_modulo("Vacantes", generar_vacantes, limpiar_vacantes, 
        [desc_est_vac, desc_estat_vac, desc_cat_vac, desc_fec_vac, transformar_datos_vacante, integrar_graficos_vacantes])
    
    # 3. Aspirantes (Inyectados sus gráficos de barra y torta de aspirantes)
    registros_totales += ejecutar_modulo("Aspirantes", generar_simulacion_aspirantes, limpiar_datos_aspirantes, 
        [describir_estructura_aspirantes, estadisticas_aspirantes, analizar_categoricas_aspirantes, analizar_fechas_aspirantes, transformar_datos_aspirantes, integrar_graficos_aspirantes])
    
    # 4. Personas (Inyectados sus gráficos de personas por ciudad)
    registros_totales += ejecutar_modulo("Personas", generar_Personas, limpiar_personas, 
        [desc_est_per, desc_estat_per, transformar_datos_persona, integrar_graficos_personas])
    
    # 5. Procesos de Selección (Inyectado su gráfico de aprobados por etapa)
    registros_totales += ejecutar_modulo("Procesos de Selección", generar_procesos, limpiar_procesos, 
        [desc_est_proc, desc_estat_proc, desc_cat_proc, desc_fec_proc, transformar_procesos, integrar_graficos_seleccion])

    print("\n" + "#"*65)
    print(f"RESUMEN DE INTEGRACIÓN FINALIZADO")
    print(f"Total de registros limpios procesados: {registros_totales}")
    print("#"*65 + "\n")

if __name__ == "__main__":
    main()