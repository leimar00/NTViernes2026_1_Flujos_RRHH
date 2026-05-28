import matplotlib.pyplot as plt
import os

RUTA_ASSETS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "mi-app-react",
    "src",
    "assets",
    "graficos_vacantes"
)


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_barras_vacantes(
        datos_agrupados,
        columna_categorias,
        columna_valores,
        titulo="Gráfico de vacantes",
        color_barras="#1565C0",
        nombre_archivo="vacantes_barras.png",
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
    print(f"Gráfico de barras de vacantes guardado en: {ruta_completa}")


def graficar_torta_vacantes(
        datos_agrupados,
        columna_etiquetas,
        columna_valores,
        titulo="Distribución de vacantes",
        lista_colores=None,
        nombre_archivo="vacantes_torta.png",
        ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)
    if lista_colores is None:
        lista_colores = [
            "#1565C0",
            "#2E7D32",
            "#E65100",
            "#6A1B9A",
            "#B71C1C"
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
    print(f"Gráfico de torta de vacantes guardado en: {ruta_completa}")


def graficar_todo_vacantes(transformacion, ruta_destino=RUTA_ASSETS):
    # Vacantes alta demanda → barras por cargo vs promedio salario
    graficar_barras_vacantes(
        datos_agrupados=transformacion["vacantesAltaDemanda"],
        columna_categorias="tituloCargo",
        columna_valores="promedio_salario",
        titulo="Promedio de salario por cargo (vacantes > $2800)",
        nombre_archivo="vacantes_alta_demanda.png",
        ruta_destino=ruta_destino
    )

    # Departamentos activos → barras por cargo vs cantidad de vacantes
    graficar_barras_vacantes(
        datos_agrupados=transformacion["departamentosActivos"],
        columna_categorias="tituloCargo",
        columna_valores="cantidad_vacantes",
        titulo="Departamentos con más vacantes activas",
        nombre_archivo="vacantes_departamentos_activos.png",
        ruta_destino=ruta_destino
    )

    # Posición developer → torta por cargo
    graficar_torta_vacantes(
        datos_agrupados=transformacion["posicionDeveloper"],
        columna_etiquetas="tituloCargo",
        columna_valores="cantidad",
        titulo="Distribución de posiciones Developer por cargo",
        nombre_archivo="vacantes_posicion_developer.png",
        ruta_destino=ruta_destino
    )

    # Vacantes abiertas → torta por fecha
    graficar_torta_vacantes(
        datos_agrupados=transformacion["vacantesAbiertas"],
        columna_etiquetas="fecha_vacante",
        columna_valores="cantidad_vacantes",
        titulo="Vacantes abiertas por fecha",
        nombre_archivo="vacantes_abiertas.png",
        ruta_destino=ruta_destino
    )