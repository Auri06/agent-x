import pygame
from utils.constants import Constants


class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 32
        self.x = max(0, min(self.x, Constants.alto_ventana-self.size))
        self.y = max(0, min(self.y, Constants.ancho_ventana-self.size))

    def spawn(self, pantalla):
        pygame.draw.rect(
            pantalla, Constants.rojo_enemigo, (self.x, self.y, self.size, self.size))
