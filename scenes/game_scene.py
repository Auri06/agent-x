import pygame
import sys
from entities.player.personaje import Agente
from map.mapa import Map
from entities.enemy.enemigo import Zombie
from utils.constants import Constants
from utils.game_window import GameWindow

ventana = GameWindow.get_instance()


def iniciar_juego():
    relog = pygame.time.Clock()
    mundo = Map(Constants.alto_mapa, Constants.ancho_mapa)
    agente = Agente(300, 340, mundo)

    # Crear zombies en posiciones válidas
    zombies = []
    for _ in range(2):
        x, y = mundo.encontrar_posicion_spawn_valida()
        zombie = Zombie(x=x, y=y, grid=mundo.obtener_grid(), mapa=mundo)
        zombies.append(zombie)

    for zombie in zombies:
        zombie.agregar_objetivo(agente)
    for zombie in zombies:
        zombie.agregar_objetivo(agente)

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        except Exception as e:
            print(f"Error handling events: {e}")
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
