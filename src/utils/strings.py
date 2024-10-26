class Strings:
    """Clase que contiene todos los strings del juego"""

    # Menú principal
    class Menu:
        TITLE = ""
        START_GAME = "Iniciar Juego"
        OPTIONS = "Opciones"
        EXIT = "Salir"
        PRESS_START = "Presiona ENTER para comenzar"

    # Juego
    class Game:
        PAUSED = "PAUSA"
        CONTINUE = "Continuar"
        RESTART = "Reiniciar"
        QUIT_TO_MENU = "Volver al Menú"

    # Game Over
    class GameOver:
        TITLE = "¡JUEGO TERMINADO!"
        WIN_MESSAGE = "¡Felicidades! ¡Has Ganado!"
        LOSE_MESSAGE = "¡Has Perdido!"
        PLAY_AGAIN = "Jugar de Nuevo"
        MAIN_MENU = "Menú Principal"

    # Mensajes de sistema
    class System:
        LOADING = "Cargando..."
        ERROR = "¡Error!"
        CONFIRM_EXIT = "¿Estás seguro que deseas salir?"
        YES = "Sí"
        NO = "No"
