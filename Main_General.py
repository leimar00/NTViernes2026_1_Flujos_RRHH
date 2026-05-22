# ============================================================================
# SISTEMA INTEGRADO DE TALENTO HUMANO - RRHH 2026
# Líder Técnico: Leimar Henao Zapata
# Institución: CESDE - Medellín, Colombia
# ============================================================================

import pandas as pd

# ============================================================================
# 1. IMPORTACIÓN DE MÓDULOS (Integración de piezas listas)
# ============================================================================

# Módulo Entrevistas (Tu trabajo - Leimar Henao Zapata)
from utils.simulacionDatosEntrevista import generarEntrevista
from noteBook.Limpieza_Entrevista import limpiar_entrevistas
from noteBook.Descripcion_Entrevista import (
    describir_estructura_entrevistas, 
    describir_estadisticas_entrevistas,
    describir_categoricas_entrevistas
)
# IMPORTACIÓN CORREGIDA: Apuntando al nuevo archivo en plural
from noteBook.transformacion_entrevistas import transformar_datos_servicio

# Módulo Aspirantes (Esteban Velandia)
from utils.aspirantes_simulacion import generar_simulacion_aspirantes
from noteBook.aspirantes_limpieza import limpiar_datos_aspirantes
from noteBook.aspirantes_descripcion import (
    describir_estructura_aspirantes, 
    estadisticas_aspirantes,
    analizar_categoricas_aspirantes,
    analizar_fechas_aspirantes
)

# Módulo Personas (El de tu compañero)
from utils.simulacion_Persona import generar_Personas
from noteBook.limpieza_persona import limpiar_simulacion as limpiar_personas
from noteBook.descripcion_persona import (
    describir_estructura as desc_est_per, 
    describir_estadisticas as desc_estat_per
)
# AGREGADO: Importación directa de la transformación de personas
from noteBook.transformacion_personas import transformar_datos_persona

# Módulo Procesos de Selección
from utils.simulacion_proceso_seleccion import generar_procesos
from noteBook.limpieza_proceso_seleccion import limpiar_procesos
from noteBook.descripcion_proceso_seleccion import (
    describir_estructura as desc_est_proc, 
    describir_estadisticas as desc_estat_proc,
    describir_categoricas as desc_cat_proc,
    describir_fechas as desc_fec_proc
)

# ============================================================================
# 2. ORQUESTADOR DE MÓDULOS (Tu diseño genérico)
# ============================================================================

def ejecutar_modulo(nombre, func_sim, func_limp, funcs_desc):
    """Lógica estándar: Simular -> DataFrame -> Limpiar -> Reportar"""
    print(f"\n" + "="*50)
    print(f">>> MÓDULO: {nombre.upper()} <<<")
    print("="*50)
    
    try:
        datos = func_sim(50)
        df = pd.DataFrame(datos)
        df_limpio = func_limp(df)
        
        for f_desc in funcs_desc:
            f_desc(df_limpio)
            
        return len(df_limpio)
    except Exception as e:
        print(f"⚠️ Nota de Integración: {nombre} tuvo un inconveniente. Detalle: {e}")
        return 0

# ============================================================================
# 3. FLUJO PRINCIPAL (Ejecución Integral)
# ============================================================================

def main():
    print("\n" + "#"*60)
    print("   SISTEMA INTEGRADO DE TALENTO HUMANO - CESDE 2026")
    print("   Líder Técnico: Leimar Henao Zapata")
    print("#"*60)

    registros_totales = 0

    # 1. Entrevistas (Módulo propio - Perfectamente acoplado en plural)
    registros_totales += ejecutar_modulo(
        "Entrevistas", 
        generarEntrevista, 
        limpiar_entrevistas, 
        [
            describir_estructura_entrevistas, 
            describir_estadisticas_entrevistas, 
            describir_categoricas_entrevistas,
            transformar_datos_servicio  
        ]
    )
    
    # 2. Aspirantes
    registros_totales += ejecutar_modulo(
        "Aspirantes", 
        generar_simulacion_aspirantes, 
        limpiar_datos_aspirantes, 
        [describir_estructura_aspirantes, estadisticas_aspirantes, analizar_categoricas_aspirantes, analizar_fechas_aspirantes]
    )
    
    # 3. Personas (Agregada tu transformación en la lista de descripción/reporte)
    registros_totales += ejecutar_modulo(
        "Personas", 
        generar_Personas, 
        limpiar_personas, 
        [
            desc_est_per, 
            desc_estat_per,
            transformar_datos_persona  # <-- Agregada igual que la tuya
        ]
    )
    
    # 4. Procesos de Selección
    registros_totales += ejecutar_modulo(
        "Procesos de Selección", 
        generar_procesos, 
        limpiar_procesos, 
        [desc_est_proc, desc_estat_proc, desc_cat_proc, desc_fec_proc]
    )

    print("\n" + "#"*60)
    print(f"RESUMEN DE INTEGRACIÓN FINALIZADO")
    print(f"Total de registros procesados por el sistema: {registros_totales}")
    print("#"*60 + "\n")

if __name__ == "__main__":
    main()