# Se importa matplotlib para crear los gráficos
import matplotlib.pyplot as plt
# Se importa os para manejar rutas y crear carpetas
import os

# Ruta típica de la carpeta assets en un proyecto React con Vite
RUTA_ASSETS = os.path.join(os.path.dirname(__file__), "..", "..", "RRHH-FRONT", "src", "assets", "graficos_proceso_seleccion")


def crear_ruta_si_no_existe(ruta_destino):
    # Se crea la carpeta destino en caso de que aún no exista
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_aprobados_por_estado(datos_agrupados, columna_categorias="estadoProceso",
                                   columna_valores="conteo",
                                   titulo="Candidatos aprobados por etapa del proceso",
                                   color_barras="#4CAF50",
                                   nombre_archivo="barras_proceso_seleccion.png",
                                   ruta_destino=RUTA_ASSETS):
    # Dibuja un gráfico de barras verticales con los candidatos que obtuvieron
    # puntaje >= 60, agrupados por etapa del proceso de selección

    # Se asegura de que la carpeta donde se guardará la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Se crea la figura y el área de dibujo con un tamaño de 10 de ancho por 5 de alto
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    # Se dibujan las barras con el color recibido y borde negro para mejor contraste
    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )

    # Se coloca el título del gráfico con tamaño de fuente 14
    area_dibujo.set_title(titulo, fontsize=14)

    # Se coloca la etiqueta del eje horizontal
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)

    # Se coloca la etiqueta del eje vertical
    area_dibujo.set_ylabel(columna_valores, fontsize=12)

    # Se rotan las etiquetas del eje X a 45 grados para evitar sobreposición
    plt.xticks(rotation=45)

    # Se ajusta el espaciado para que nada quede cortado
    plt.tight_layout()

    # Se construye la ruta completa del archivo y se guarda la imagen
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)

    # Se cierra la figura para liberar memoria
    plt.close(figura)

    # Se imprime la ubicación donde quedó guardada la imagen
    print(f"Gráfico de barras guardado en: {ruta_completa}")