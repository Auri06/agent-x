# main.py

import pygame
import sys
from entities.player.personaje import Agente
from map.mapa import Map
from entities.enemy.enemigo import Zombie
from utils.constants import Constants

pygame.init()

ventana = pygame.display.set_mode(
    (Constants.alto_ventana, Constants.ancho_ventana))
pygame.display.set_caption("angete x")


def main():
    relog = pygame.time.Clock()
    mundo = Map(Constants.alto_mapa, Constants.ancho_mapa)
    agente = Agente(300, 340, mundo)

    # Crear zombies con acceso a la grid del mapa y a las colisiones
    zombies = [
        Zombie(x=100, y=100, grid=mundo.obtener_grid(), mapa=mundo),
        Zombie(x=200, y=200, grid=mundo.obtener_grid(), mapa=mundo),
    ]

    for zombie in zombies:
        zombie.agregar_objetivo(agente)

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

        for zombie in zombies:
            zombie.actualizar()
            zombie.spawn(ventana)

        pygame.display.flip()
        relog.tick(58)


if __name__ == "__main__":
    main()
