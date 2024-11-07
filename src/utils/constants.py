from pathlib import Path
from assets import images 
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
    quieto1:Path= Path("assets/images/player/quieto1.png")
    quieto2:Path= Path("assets/images/player/quieto2.png")
    quieto3:Path= Path("assets/images/player/quieto3.png")

    down1:Path= Path("assets/images/player/down1.png")
    down2:Path= Path("assets/images/player/down2.png")
    down3:Path= Path("assets/images/player/down3.png")
    down4:Path= Path("assets/images/player/down4.png")
    
    up1:Path= Path("assets/images/player/up1.png")
    up2:Path= Path("assets/images/player/up2.png")
    up3:Path= Path("assets/images/player/up3.png")
    up4:Path= Path("assets/images/player/up4.png")
    
    walk1:Path= Path("assets/images/player/walk1.png")
    walk2:Path= Path("assets/images/player/walk2.png")
   
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
