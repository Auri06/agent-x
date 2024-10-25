
import pygame
import sys
from personaje import Agente
from mapa import Map
from enemigo import Zombie
pygame.init()

alto = 800
ancho = 700


ventana = pygame.display.set_mode((alto,ancho))
pygame.display.set_caption("angete x")

blanco="white"
verde = "green"
rojo= "red"
gris="grey"


def main ():
    relog = pygame.time.Clock()
    mundo= Map(alto,ancho)
    agente= Agente(300,340,mundo)
    zombie0=Zombie(0,150)
    zombie1=Zombie(600,150)
    zombie2=Zombie(0,150)
    zombie3=Zombie(100,530)
    zombie4=Zombie(600,340)
    zombie5=Zombie(300,630)
    zombie6=Zombie(720,40)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT]:
                agente.movimiento(-5, 0)
        if teclas[pygame.K_RIGHT]:
                agente.movimiento(5, 0)
        if teclas[pygame.K_UP]:
                agente.movimiento(0, -5)
        if teclas[pygame.K_DOWN]:
                agente.movimiento(0, 5)
        

        mundo.spawn(ventana)
        agente.spawn(ventana)
        zombie0.spawn(ventana)
        zombie1.spawn(ventana)
        zombie2.spawn(ventana)
        zombie3.spawn(ventana)
        zombie4.spawn(ventana)
        zombie5.spawn(ventana)
        zombie6.spawn(ventana)
        pygame.display.flip()
        relog.tick(58)
if __name__ == "__main__":
    main()              