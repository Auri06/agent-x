import pygame




class Agente:
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.size = 32
        self.mapa = mapa  

    def spawn(self, pantalla):
        pygame.draw.rect(pantalla, verde, (self.x, self.y, self.size, self.size))

    def movimiento(self, dx, dy):
        
        nuevo_x = self.x + dx
        nuevo_y = self.y + dy

       
        nuevo_rect = pygame.Rect(nuevo_x, nuevo_y, self.size, self.size)

        
        if not self.colision_mapa(nuevo_rect):
            self.x = nuevo_x
            self.y = nuevo_y
            
        self.x = max(0, min(self.x, ancho - self.size))
        self.y = max(0, min(self.y, alto - self.size))

    def colision_mapa(self, nuevo_rect):
        # Verificar colisiones con los bloques del mapa
        for bloque in self.mapa.obtener_rectangulos():
            if nuevo_rect.colliderect(bloque):
                return True
        return False
