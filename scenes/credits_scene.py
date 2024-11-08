import pygame
import sys
from utils.constants import Constants
from utils.game_window import GameWindow

ventana = GameWindow.get_instance()


def mostrar_creditos():
    pygame.event.clear()

    # Configuración de fuentes y colores
    titulo_font = pygame.font.Font(None, 100)
    subtitulo_font = pygame.font.Font(None, 70)
    texto_font = pygame.font.Font(None, 50)
    color_titulo = (255, 255, 255)
    color_subtitulo = (255, 255, 0)
    color_texto = (200, 200, 200)

    # Estructura de créditos organizada por secciones
    creditos = {
        "DESARROLLO": [
            "Programación: Auri Eliezer",
            "Musica: Artista Y",
            "Imagenes: Artista U",
            "Efectos: Persona Z",
            "Agradecimientos: Persona U"
        ]
    }

    while True:
        ventana.fill((0, 0, 0))

        # Renderizar título principal
        titulo = titulo_font.render('Créditos', True, color_titulo)
        titulo_rect = titulo.get_rect(
            center=(Constants.ancho_ventana // 2, 80)
        )
        ventana.blit(titulo, titulo_rect)

        # Posición inicial para las secciones
        y_pos = 180
        espaciado_seccion = 50
        espaciado_items = 35

        # Renderizar cada sección
        for seccion, items in creditos.items():
            # Renderizar subtítulo de sección
            subtitulo = subtitulo_font.render(seccion, True, color_subtitulo)
            subtitulo_rect = subtitulo.get_rect(
                center=(Constants.ancho_ventana // 2, y_pos)
            )
            ventana.blit(subtitulo, subtitulo_rect)
            y_pos += espaciado_seccion

            # Renderizar items de la sección
            for item in items:
                texto = texto_font.render(item, True, color_texto)
                texto_rect = texto.get_rect(
                    center=(Constants.ancho_ventana // 2, y_pos)
                )
                ventana.blit(texto, texto_rect)
                y_pos += espaciado_items

            y_pos += espaciado_seccion  # Espacio extra entre secciones

        # Renderizar mensaje de salida
        salir_texto = texto_font.render(
            'Presiona cualquier tecla para volver', True, (128, 128, 128))
        salir_rect = salir_texto.get_rect(
            center=(Constants.ancho_ventana // 2, Constants.alto_ventana - 40)
        )
        ventana.blit(salir_texto, salir_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.event.clear()
                return

        pygame.display.flip()
