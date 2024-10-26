class Constants:
    "Clase que contiene todas las constantes del proyecto"

    # * Configuracion de la ventana
    alto_ventana = 800
    ancho_ventana = 700

    # * Colores (RGB)
    COLOR_FONDO = (0, 0, 0)  # ? Abierto a cambios
    color_primario = (255, 255, 255)  # ? Abierto a cambios
    color_secundario = (0, 0, 0)   # ? Abierto a cambios
    color_accent = (255, 0, 0)     # ? Abierto a cambios

    # * Personaje
    VERDE_PERSONAJE = (54, 255, 51)

    # * Enemigos
    rojo_enemigo = (255, 0, 0)

    # * Mapa
    blanco_mapa = (255, 255, 255)
    alto_mapa = 800
    ancho_mapa = 700

    # * Bloques
    BLOCK_COLOR = (200, 200, 200)
    BLOCK_SIZE = 50


class Assets:
    "Clase que contiene el path de todos los assets del juego"

    # * Personaje
    PERSONAJE_QUIETO = ""
    PERSONAJE_CAMINAR_FRENTE = ""
    PERSONAJE_CAMINAR_ATRAS = ""
    PERSONAJE_CAMINAR_DERECHA = ""
    PERSONAJE_CAMINAR_IZQUIERDA = ""


    # * Enemigos
    ENEMIGO_QUIETO = ""
    ENEMIGO_CAMINAR_FRENTE = ""
    ENEMIGO_CAMINAR_ATRAS = ""
    ENEMIGO_CAMINAR_DERECHA = ""
    ENEMIGO_CAMINAR_IZQUIERDA = ""

    # * Mapa

    # * Otros

    # * Música
    MENU_MUSIC = ""
    GAME_MUSIC = ""
    VICTORY_MUSIC = ""
    GAME_OVER_MUSIC = ""
