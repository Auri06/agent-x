import pygame
from utils.constants import Constants


class Map:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.BLOCK_SIZE = 50
        self.espacio = 45

    def spawn(self, pantalla):
        pantalla.fill(Constants.BLOCK_COLOR)

        filas = 9
        columnas = 9
        self.rectangulos = []  # Para almacenar los rectángulos

        for fila in range(filas):
            for columna in range(columnas):
                x = columna * (self.BLOCK_SIZE + self.espacio)
                y = fila * (self.BLOCK_SIZE + self.espacio)

                rect = pygame.draw.rect(
                    pantalla, Constants.COLOR_FONDO, (x, y, self.BLOCK_SIZE, self.BLOCK_SIZE))
                # Guardar el rectángulo para colisiones
                self.rectangulos.append(rect)

    def obtener_rectangulos(self):
        return self.rectangulos
