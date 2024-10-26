import pygame




class Map:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.bloque_tamaño = 50
        self.espacio = 45

    def spawn(self, pantalla):
        pantalla.fill(gris)

        filas = 9
        columnas = 9
        self.rectangulos = []  # Para almacenar los rectángulos

        for fila in range(filas):
            for columna in range(columnas):
                x = columna * (self.bloque_tamaño + self.espacio)
                y = fila * (self.bloque_tamaño + self.espacio)

                rect = pygame.draw.rect(pantalla, blanco, (x, y, self.bloque_tamaño, self.bloque_tamaño))
                self.rectangulos.append(rect)  # Guardar el rectángulo para colisiones

    def obtener_rectangulos(self):
        return self.rectangulos
