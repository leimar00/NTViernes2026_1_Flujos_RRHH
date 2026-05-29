import matplotlib.pyplot as plt
import os

# ── CONFIGURACIÓN DE LA RUTA HACIA EL FRONTEND ──
# NOTA: Si la carpeta de React de tu amigo no se llama "mi-app-react",
# cambia ese nombre por el correcto aquí abajo (ej: "frontend", "react-app").
RUTA_ASSETS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "mi-app-react", 
    "src",
    "assets",
    "graficos_entrevistas"
)


def asegurar_carpeta_existente():
    """Revisa si la carpeta existe en React, si no, la crea automáticamente."""
    os.makedirs(RUTA_ASSETS, exist_ok=True)


def graficar_barras_entrevistas(datos_agrupados, columna_categorias, columna_valores, titulo="Estados de Entrevistas Activas"):
    """Genera el gráfico de barras y lo exporta como imagen PNG a React."""
    if datos_agrupados.empty:
        print("⚠️ Gráfico Barras: No hay datos para graficar.")
        return

    asegurar_carpeta_existente()

    # Crear el lienzo del gráfico
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    # Dibujar las barras (Color morado elegante para distinguir tu módulo)
    area_dibujo.bar(
        datos_agrupados[columna_categorias].astype(str),
        datos_agrupados[columna_valores],
        color="#9C27B0",
        edgecolor="black"
    )

    # Personalizar títulos y etiquetas
    area_dibujo.set_title(titulo, fontsize=13, fontweight='bold')
    area_dibujo.set_xlabel(columna_categorias, fontsize=11)
    area_dibujo.set_ylabel(columna_valores, fontsize=11)

    plt.xticks(rotation=35, ha='right')  # Rotación para evitar que se pisen los textos
    plt.tight_layout()

    # Guardar directamente en la carpeta de React
    ruta_completa = os.path.join(RUTA_ASSETS, "entrevistas_barras.png")
    figura.savefig(ruta_completa)
    plt.close(figura)  # Cerrar gráfico para liberar memoria

    print(f"✅ Gráfico de barras guardado en el Front: {ruta_completa}")


def graficar_torta_entrevistas(datos_agrupados, columna_etiquetas, columna_valores, titulo="Distribución de Entrevistas"):
    """Genera el gráfico de torta (porcentajes) y lo exporta como PNG a React."""
    if datos_agrupados.empty:
        print("⚠️ Gráfico Torta: No hay datos para graficar.")
        return

    asegurar_carpeta_existente()

    # Paleta de colores vivos y profesionales
    colores_paleta = ["#9C27B0", "#00BCD4", "#4CAF50", "#FF9800", "#E91E63"]
    cantidad_categorias = len(datos_agrupados)

    figura, area_dibujo = plt.subplots(figsize=(7, 7))

    # Dibujar la torta
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas].astype(str),
        autopct="%1.1f%%",  # Muestra el porcentaje con un decimal
        colors=colores_paleta[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.8}
    )

    area_dibujo.set_title(titulo, fontsize=13, fontweight='bold')
    plt.tight_layout()

    # Guardar en la carpeta de React
    ruta_completa = os.path.join(RUTA_ASSETS, "entrevistas_torta.png")
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"✅ Gráfico de torta guardado en el Front: {ruta_completa}")