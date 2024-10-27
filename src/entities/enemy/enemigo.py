from ai.behavior_tree.enemy.behavior_tree import Selector, Action, Sequence, Invert, Timer
import pygame
import random
from ai.pathfinding.a_star import AStar


class Zombie:
    def __init__(self, tiempo_atacando=3, x=0, y=0, grid=None, mapa=None):
        self.objetivo = None
        self.grid = grid  # Mapa para el algoritmo A*
        self.comportamiento = Selector([
            self.crear_secuencia_reposo(),
            self.crear_secuencia_ataque(tiempo_atacando)
        ])
        self.x = x  # Posición inicial en x
        self.y = y  # Posición inicial en y
        self.punto_patrol = (self.x, self.y)  # Punto actual de patrullaje
        self.velocidad = 2  # Velocidad del zombie
        self.mapa = mapa

    def crear_secuencia_reposo(self):
        hay_objetivo = Action(lambda: self.objetivo is not None)
        return Sequence([
            Invert(hay_objetivo),
            Action(self.patrullar)
        ])

    def crear_secuencia_ataque(self, tiempo_atacando):
        return Sequence([
            Action(self.objetivo_cerca),
            Action(self.perseguir_jugador),
            Action(self.atacar),
            Timer(tiempo_atacando, Action(self.desactivar_objetivo))
        ])

    def agregar_objetivo(self, objetivo=None):
        self.objetivo = objetivo
        print("Objetivo agregado")

    def desactivar_objetivo(self):
        self.objetivo = None
        print("Objetivo desactivado")
        return True

    def objetivo_cerca(self):
        distancia = ((self.x - self.objetivo.x) ** 2 +
                     (self.y - self.objetivo.y) ** 2) ** 0.5
        return distancia < 100

    def patrullar(self):
        print("Patrullando...")

        if random.random() < 0.05:  # Cambiar dirección con un 5% de probabilidad cada actualización
            self.punto_patrol = (random.randint(
                0, len(self.grid[0]) - 1), random.randint(0, len(self.grid) - 1))

        # Moverse hacia el punto de patrullaje usando A*
        path = AStar(self.grid).search(
            (self.x // 50, self.y // 50), self.punto_patrol)

        if path and len(path) > 1:
            next_step = path[1]  # Obtener el siguiente paso en el camino
            nuevo_rect = pygame.Rect(
                next_step[0] * 50, next_step[1] * 50, 40, 40)

            # Verificar colisión antes de mover
            if not self.colision_mapa(nuevo_rect):
                self.x, self.y = next_step[0] * 50, next_step[1] * 50

        return True

    def perseguir_jugador(self):
        print("Persiguiendo al jugador...")

        path = AStar(self.grid).search((self.x // 50, self.y // 50),
                                       (self.objetivo.x // 50, self.objetivo.y // 50))

        if path and len(path) > 1:
            next_step = path[1]  # Obtener el siguiente paso en el camino
            nuevo_rect = pygame.Rect(
                next_step[0] * 50, next_step[1] * 50, 40, 40)

            # Verificar colisión antes de mover
            if not self.colision_mapa(nuevo_rect):
                self.x, self.y = next_step[0] * 50, next_step[1] * 50

        return True

    def colision_mapa(self, nuevo_rect):
        # Verificar colisiones con los bloques del mapa
        for bloque in self.mapa.obtener_rectangulos():
            if nuevo_rect.colliderect(bloque):
                return True
        return False

    def atacar(self):
        print("Atacando al objetivo " + str(self.objetivo))
        return True

    def spawn(self, pantalla):
        color_zombie = (0, 255, 0)  # Color verde para el zombie
        tamano = 40  # Tamaño del zombie
        pygame.draw.rect(pantalla, color_zombie,
                         (self.x, self.y, tamano, tamano))

    def actualizar(self):
        self.comportamiento.run()
