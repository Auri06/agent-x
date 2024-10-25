import pygame 
rojo= "red"
alto = 800
ancho = 700
class Zombie:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.size= 32
        self.x = max(0,min(self.x,alto-self.size))
        self.y = max(0,min(self.y,ancho-self.size))
        
    def spawn(self,pantalla):
        pygame.draw.rect(pantalla, rojo, (self.x, self.y, self.size, self.size))