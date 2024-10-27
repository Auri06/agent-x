import pygame
from utils.constants import Constants


class Map:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.BLOCK_SIZE = 50
        self.espacio = 45
        self.grid = self.crear_grid()  # Inicializar la cuadrícula

    def crear_grid(self):
        # Crear una cuadrícula de ejemplo (0 = espacio libre, 1 = obstáculo)
        filas = (self.alto // (self.BLOCK_SIZE + self.espacio))
        columnas = (self.ancho // (self.BLOCK_SIZE + self.espacio))
        return [[0 for _ in range(columnas)] for _ in range(filas)]

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

    def obtener_grid(self):
        return self.grid  # Método que devuelve la cuadrícula
