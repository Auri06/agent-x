import pygame
from utils.constants import Constants, Assets


class Agente:
    def __init__(self, x, y, mapa):
        self.x = x
        self.y = y
        self.size = 32
        self.mapa = mapa
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)  # Agregar rect

        # Sprite management
        self.sprites = {
            'quieto': [pygame.image.load(str(Assets.quieto1)), pygame.image.load(str(Assets.quieto2)), 
                      pygame.image.load(str(Assets.quieto3))],
            'walk': [pygame.image.load(str(Assets.walk1)), pygame.image.load(str(Assets.walk2))],
            'up': [pygame.image.load(str(Assets.up1)), pygame.image.load(str(Assets.up2)), 
                  pygame.image.load(str(Assets.up3)), pygame.image.load(str(Assets.up4))],
            'down': [pygame.image.load(str(Assets.down1)), pygame.image.load(str(Assets.down2)), 
                    pygame.image.load(str(Assets.down3)), pygame.image.load(str(Assets.down4))]
        }
        self.current_state = 'quieto'
        self.sprite_index = 0
        self.animation_speed = 0.15  # Reduced speed for smoother animation
        self.animation_timer = 0
        self.facing_left = False

    def spawn(self, pantalla):
        self.update_animation()
        sprites_list = self.sprites[self.current_state]
        # Ensure valid index
        if self.sprite_index >= len(sprites_list):
            self.sprite_index = 0
        current_sprite = sprites_list[self.sprite_index]
        if self.facing_left:
            current_sprite = pygame.transform.flip(current_sprite, True, False)
        pantalla.blit(current_sprite, (self.x, self.y))

    def update_animation(self):
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            max_frames = len(self.sprites[self.current_state])
            self.sprite_index = (self.sprite_index + 1) % max_frames
            # Ensure sprite_index is always valid
            if self.sprite_index >= max_frames:
                self.sprite_index = 0

    def movimiento(self, dx, dy):

        nuevo_x = self.x + dx
        nuevo_y = self.y + dy

        nuevo_rect = pygame.Rect(nuevo_x, nuevo_y, self.size, self.size)

        if not self.colision_mapa(nuevo_rect):
            self.x = nuevo_x
            self.y = nuevo_y
            self.rect.x = self.x  # Actualizar posición del rect
            self.rect.y = self.y
            
            # Update animation state based on movement
            if dx != 0 or dy != 0:
                if abs(dy) > abs(dx):
                    self.current_state = 'down' if dy > 0 else 'up'
                else:
                    self.current_state = 'walk'
                    # Cambiar la dirección del sprite: ahora facing_left es True cuando va a la derecha
                    self.facing_left = dx > 0  # Invertimos la lógica aquí
            else:
                self.current_state = 'quieto'

        self.x = max(0, min(self.x, Constants.ancho_ventana - self.size))
        self.y = max(0, min(self.y, Constants.alto_ventana - self.size))

    def colision_mapa(self, nuevo_rect):
        # Verificar colisiones con los bloques del mapa
        for bloque in self.mapa.obtener_rectangulos():
            if nuevo_rect.colliderect(bloque):
                return True
        return False
