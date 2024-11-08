import pygame
from utils.constants import Constants

class GameWindow:
    _instance = None
    _initialized = False

    @classmethod
    def get_instance(cls):
        if not cls._initialized:
            pygame.init()
            cls._initialized = True
        
        if cls._instance is None:
            cls._instance = pygame.display.set_mode(
                (Constants.ancho_ventana, Constants.alto_ventana))
            pygame.display.set_caption("agente x")
        return cls._instance
