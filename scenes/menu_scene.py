import pygame
import sys
from scenes.credits_scene import mostrar_creditos
from utils.constants import Constants
from utils.game_window import GameWindow
from scenes.game_scene import iniciar_juego

ventana = GameWindow.get_instance()

def mostrar_menu():
    pygame.event.clear()
    opciones = ['Inicio', 'Creditos', 'Salir']
    indice_seleccionado = 0

    # Configuración de fuentes y colores
    titulo_font = pygame.font.Font(None, 100)
    menu_font = pygame.font.Font(None, 64)
    color_seleccionado = (255, 255, 0)
    color_normal = (128, 128, 128)
    
    while True:
        ventana.fill((0, 0, 0))

        # Centrar título en el tercio superior de la pantalla
        titulo = titulo_font.render('Agent X', True, (255, 255, 255))
        titulo_rect = titulo.get_rect(
            center=(Constants.ancho_ventana // 2, Constants.alto_ventana // 3)
        )
        ventana.blit(titulo, titulo_rect)

        # Centrar menú verticalmente
        total_menu_height = len(opciones) * 70  # altura total del menú
        menu_y_start = (Constants.alto_ventana - total_menu_height) // 2 + 50  # añadir offset para balance visual

        # Renderizar opciones del menú
        for i, opcion in enumerate(opciones):
            color = color_seleccionado if i == indice_seleccionado else color_normal
            text = menu_font.render(opcion, True, color)
            
            # Calcular posición central para el indicador
            if i == indice_seleccionado:
                indicador = menu_font.render('>', True, color_seleccionado)
                indicador_rect = indicador.get_rect(
                    right=Constants.ancho_ventana//2 - 100,
                    centery=menu_y_start + i * 70
                )
                ventana.blit(indicador, indicador_rect)

            # Centrar cada opción
            text_rect = text.get_rect(
                center=(Constants.ancho_ventana//2, menu_y_start + i * 70)
            )
            ventana.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if indice_seleccionado == 0:
                        pygame.event.clear()
                        iniciar_juego()
                        return
                    elif indice_seleccionado == 1:
                        pygame.event.clear()
                        mostrar_creditos()
                    elif indice_seleccionado == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP:
                    indice_seleccionado = (indice_seleccionado - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    indice_seleccionado = (indice_seleccionado + 1) % len(opciones)

        pygame.display.flip()
