# ============================================================================
# SISTEMA INTEGRADO DE TALENTO HUMANO - RRHH 2026
# Líder Técnico de Integración: Leimar Henao Zapata
# Institución: CESDE - Medellín, Colombia
# ============================================================================

import pandas as pd

# ============================================================================
# 1. IMPORTACIÓN DE MÓDULOS (Ajustado a nombres reales de archivos)
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

# ── Módulo Vacantes (Basado en tu árbol de archivos) ──
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

# ── Módulo Personas ──
from utils.simulacion_Persona import generar_Personas
from noteBook.limpieza_persona import limpiar_simulacion as limpiar_personas
from noteBook.descripcion_persona import (
    describir_estructura as desc_est_per, 
    describir_estadisticas as desc_estat_per
)

# ── Módulo Procesos de Selección ──
from utils.simulacion_proceso_seleccion import generar_procesos
from noteBook.limpieza_proceso_seleccion import limpiar_procesos
from noteBook.descripcion_proceso_seleccion import (
    describir_estructura as desc_est_proc, 
    describir_estadisticas as desc_estat_proc,
    describir_categoricas as desc_cat_proc,
    describir_fechas as desc_fec_proc
)

# ============================================================================
# 2. ORQUESTADOR DE MÓDULOS
# ============================================================================

def ejecutar_modulo(nombre, func_sim, func_limp, funcs_desc):
    print(f"\n" + "="*55)
    print(f">>> MÓDULO: {nombre.upper()} <<<")
    print("="*55)
    
    try:
        datos = func_sim(50)
        df = pd.DataFrame(datos)
        df_limpio = func_limp(df)
        
        for f_desc in funcs_desc:
            # Manejo especial para la función de transformación que retorna dict
            if f_desc.__name__ == "transformar_datos_vacante":
                print("\n⚙️ Ejecutando matrices de transformación para Vacantes...")
                resultado_dicc = f_desc(df_limpio)
                print(f"   -> Transformación completada. Diccionario con {len(resultado_dicc)} dataframes generado.")
            else:
                f_desc(df_limpio)
            
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

    # 1. Entrevistas
    registros_totales += ejecutar_modulo("Entrevistas", generarEntrevista, limpiar_entrevistas, 
        [describir_estructura_entrevistas, describir_estadisticas_entrevistas, describir_categoricas_entrevistas, transformar_datos_servicio])
    
    # 2. Vacantes
    registros_totales += ejecutar_modulo("Vacantes", generar_vacantes, limpiar_vacantes, 
        [desc_est_vac, desc_estat_vac, desc_cat_vac, desc_fec_vac, transformar_datos_vacante])
    
    # 3. Aspirantes
    registros_totales += ejecutar_modulo("Aspirantes", generar_simulacion_aspirantes, limpiar_datos_aspirantes, 
        [describir_estructura_aspirantes, estadisticas_aspirantes, analizar_categoricas_aspirantes, analizar_fechas_aspirantes])
    
    # 4. Personas
    registros_totales += ejecutar_modulo("Personas", generar_Personas, limpiar_personas, 
        [desc_est_per, desc_estat_per])
    
    # 5. Procesos de Selección
    registros_totales += ejecutar_modulo("Procesos de Selección", generar_procesos, limpiar_procesos, 
        [desc_est_proc, desc_estat_proc, desc_cat_proc, desc_fec_proc])

    print("\n" + "#"*65)
    print(f"RESUMEN DE INTEGRACIÓN FINALIZADO")
    print(f"Total de registros limpios procesados: {registros_totales}")
    print("#"*65 + "\n")

if __name__ == "__main__":
    main()