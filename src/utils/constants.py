from enum import Enum


class Constants:
    "Clase que contiene todas las constantes del proyecto"

    # * Configuracion de la ventana
    alto_ventana = 800
    ancho_ventana = 700

    # * Colores (RGB)
    color_fondo = (0, 0, 0)  # ? Abierto a cambios
    color_primario = (255, 255, 255)  # ? Abierto a cambios
    color_secundario = (0, 0, 0)   # ? Abierto a cambios
    color_accent = (255, 0, 0)     # ? Abierto a cambios

    # * Colores entidades
    rojo_enemigo = (255, 0, 0)
    verde_personaje = (54, 255, 51)
    gris_bloke = (200, 200, 200)

    # * Mapa
    blanco_mapa = (255, 255, 255)
    alto_mapa = 800
    ancho_mapa = 700


class Assets:
    "Clase que contiene el path de todos los assets del juego"

    # * Personaje

    # * Enemigos

    # * Mapa

    # * Otros

    #* Música
    MENU_MUSIC = ""
    GAME_MUSIC = ""
    VICTORY_MUSIC = ""
    GAME_OVER_MUSIC = ""

    