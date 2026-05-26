import matplotlib.pyplot as plt
import os

RUTA_ASSETS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "mi-app-react",
    "src",
    "assets",
    "graficos_aspirantes"
)


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_barras_aspirantes(
        datos_agrupados,
        columna_categorias,
        columna_valores,
        titulo="Gráfico de aspirantes",
        color_barras="#1976D2",
        nombre_archivo="aspirantes_barras.png",
        ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )

    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico de barras de aspirantes guardado en: {ruta_completa}")


def graficar_torta_aspirantes(
        datos_agrupados,
        columna_etiquetas,
        columna_valores,
        titulo="Distribución de aspirantes",
        lista_colores=None,
        nombre_archivo="aspirantes_torta.png",
        ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if lista_colores is None:
        lista_colores = [
            "#1976D2",
            "#388E3C",
            "#F57C00",
            "#7B1FA2",
            "#D32F2F"
        ]

    figura, area_dibujo = plt.subplots(figsize=(8, 8))

    cantidad_categorias = len(datos_agrupados)

    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={
            "edgecolor": "black",
            "linewidth": 0.5
        }
    )

    area_dibujo.set_title(titulo, fontsize=14)

    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico de torta de aspirantes guardado en: {ruta_completa}")