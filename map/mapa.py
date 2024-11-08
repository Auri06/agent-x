import random
import pygame
from utils.constants import Assets, Constants


class Map:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.BLOCK_SIZE = 50
        self.espacio = 45
        self.rectangulos = []
        self.tile_image = pygame.image.load(Assets.TILES)
        self.tile_image = pygame.transform.scale(
            self.tile_image, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.grid = self.crear_grid()

    def crear_grid(self):
        # Crear una cuadrícula basada en el tamaño total del mapa
        filas = self.alto // 50
        columnas = self.ancho // 50
        # Inicializar todo como espacio transitable (0)
        grid = [[0 for _ in range(columnas)] for _ in range(filas)]

        # Marcar los bloques como obstáculos (1)
        for fila in range(9):
            for columna in range(9):
                x = columna * (self.BLOCK_SIZE + self.espacio)
                y = fila * (self.BLOCK_SIZE + self.espacio)

                # Convertir coordenadas de píxeles a índices de grid
                grid_x = x // 50
                grid_y = y // 50

                # Marcar el bloque y su área como obstáculo
                if grid_y < len(grid) and grid_x < len(grid[0]):
                    grid[grid_y][grid_x] = 1

                    # Marcar el área del bloque completo
                    for dy in range(self.BLOCK_SIZE // 50):
                        for dx in range(self.BLOCK_SIZE // 50):
                            if (grid_y + dy < len(grid) and
                                    grid_x + dx < len(grid[0])):
                                grid[grid_y + dy][grid_x + dx] = 1

        return grid

    def spawn(self, pantalla):
        pantalla.fill(Constants.BLOCK_COLOR)
        self.rectangulos.clear()

        for fila in range(9):
            for columna in range(9):
                x = columna * (self.BLOCK_SIZE + self.espacio)
                y = fila * (self.BLOCK_SIZE + self.espacio)
                rect = pygame.Rect(x, y, self.BLOCK_SIZE, self.BLOCK_SIZE)
                self.rectangulos.append(rect)
                pantalla.blit(self.tile_image, rect)

    def obtener_rectangulos(self):
        return self.rectangulos

    def obtener_grid(self):  # Añadido el método que faltaba
        return self.grid

    def encontrar_posicion_spawn_valida(self):
        intentos = 0
        while intentos < 100:
            # Generar coordenadas en unidades de grid
            grid_x = random.randint(0, len(self.grid[0]) - 1)
            grid_y = random.randint(0, len(self.grid) - 1)

            # Verificar si la posición es válida en el grid
            if self.grid[grid_y][grid_x] == 0:
                # Convertir coordenadas de grid a píxeles
                x = grid_x * 50
                y = grid_y * 50
                return x, y

            intentos += 1

        # Posición por defecto si no se encuentra una válida
        return self.BLOCK_SIZE + self.espacio, self.BLOCK_SIZE + self.espacio
