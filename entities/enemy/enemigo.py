from ai.behavior_tree.enemy.behavior_tree import Selector, Action, Sequence, Invert, Timer
import pygame
import random
from ai.pathfinding.a_star import AStar
from utils.constants import Assets


class Zombie:
    def __init__(self, tiempo_atacando=3, x=0, y=0, grid=None, mapa=None):
        self.objetivo = None
        self.grid = grid  # Mapa para el algoritmo A*
        self.comportamiento = Selector([
            self.crear_secuencia_reposo(),
            self.crear_secuencia_ataque(tiempo_atacando)
        ])
        self.x = x * 1.0  # Asegurar que sea float
        self.y = y * 1.0  # Asegurar que sea float
        self.punto_patrol = (int(self.x // 50), int(self.y // 50))
        self.velocidad = 2  # Reducir velocidad para mejor control
        self.mapa = mapa
        self.sprites = {
            'quieto': [pygame.image.load(str(Assets.QUIETO1)), pygame.image.load(str(Assets.QUIETO2)),
                       pygame.image.load(str(Assets.QUIETO3)), pygame.image.load(str(Assets.QUIETO4))],
            'walk': [pygame.image.load(str(Assets.WALK1)), pygame.image.load(str(Assets.WALK2)),
                     pygame.image.load(str(Assets.WALK3)), pygame.image.load(str(Assets.WALK4))],
            'up': [pygame.image.load(str(Assets.UP1)), pygame.image.load(str(Assets.UP2)),
                   pygame.image.load(str(Assets.UP3)), pygame.image.load(str(Assets.UP4))],
            'down': [pygame.image.load(str(Assets.DOWN1)), pygame.image.load(str(Assets.DOWN2)),
                     pygame.image.load(str(Assets.DOWN3)), pygame.image.load(str(Assets.DOWN4))]
        }
        self.current_sprite = 0
        self.animation_speed = 0.2
        self.current_animation = 'quieto'
        self.facing_right = True
        self.animation_timer = 0
        self.path = None
        self.last_path_update = 0
        self.path_update_interval = 30  # Update path every 30 frames
        self.patrol_timer = 0
        self.next_patrol = random.randint(60, 120)  # Frames until next patrol point

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
        if self.objetivo is None:
            return False
        distancia = ((self.x - self.objetivo.x) ** 2 +
                     (self.y - self.objetivo.y) ** 2) ** 0.5
        esta_cerca = distancia < 200
        if esta_cerca:
            print(f"¡Objetivo detectado a {int(distancia)} pixels de distancia!")
        return esta_cerca

    def patrullar(self):
        self.patrol_timer += 1
        if self.patrol_timer >= self.next_patrol or not self.path:
            # Generate new patrol point
            intentos = 0
            while intentos < 10:
                # Generar punto aleatorio en coordenadas de grid
                grid_x = random.randint(0, len(self.grid[0]) - 1)
                grid_y = random.randint(0, len(self.grid) - 1)
                
                # Verificar si el punto es válido (no hay obstáculo)
                if self.grid[grid_y][grid_x] == 0:
                    self.punto_patrol = (grid_x, grid_y)
                    inicio = (int(self.x // 50), int(self.y // 50))
                    self.path = AStar(self.grid).search(inicio, self.punto_patrol)
                    print(f"Nueva ruta de patrulla: {self.path}")  # Debug
                    if self.path:
                        break
                intentos += 1
            
            self.patrol_timer = 0
            self.next_patrol = random.randint(60, 120)

        if self.path and len(self.path) > 1:
            next_step = self.path[1]
            target_x = next_step[0] * 50
            target_y = next_step[1] * 50

            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx**2 + dy**2)**0.5
            
            if distance > 0:
                dx = (dx / distance) * self.velocidad
                dy = (dy / distance) * self.velocidad

                nuevo_rect = pygame.Rect(self.x + dx, self.y + dy, 40, 40)
                if not self.colision_mapa(nuevo_rect):
                    self.x += dx
                    self.y += dy
                    print(f"Moviendo a: ({self.x}, {self.y})")  # Debug
                    
                    # Update animation based on movement
                    if abs(dy) > abs(dx):
                        self.current_animation = 'down' if dy > 0 else 'up'
                    else:
                        self.current_animation = 'walk'
                        self.facing_right = dx > 0

                    # Update path when reached next point
                    if abs(self.x - target_x) < self.velocidad and abs(self.y - target_y) < self.velocidad:
                        self.path.pop(0)
                else:
                    self.path = None  # Force new path calculation if blocked
        else:
            self.current_animation = 'quieto'

        return True

    def perseguir_jugador(self):
        if self.objetivo is None:
            return False

        self.last_path_update += 1
        if self.last_path_update >= self.path_update_interval or not self.path:
            start_pos = (int(self.x // 50), int(self.y // 50))
            goal_pos = (int(self.objetivo.x // 50), int(self.objetivo.y // 50))
            
            # Ensure positions are within grid bounds
            if (0 <= start_pos[0] < len(self.grid[0]) and 
                0 <= start_pos[1] < len(self.grid) and 
                0 <= goal_pos[0] < len(self.grid[0]) and 
                0 <= goal_pos[1] < len(self.grid)):
                
                self.path = AStar(self.grid).search(start_pos, goal_pos)
                self.last_path_update = 0
                print(f"New path calculated: {self.path}")  # Debug print

        if self.path and len(self.path) > 1:
            next_step = self.path[1]
            target_x = next_step[0] * 50
            target_y = next_step[1] * 50

            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx**2 + dy**2)**0.5
            
            if distance > 0:
                dx = (dx / distance) * self.velocidad * 1.5
                dy = (dy / distance) * self.velocidad * 1.5

                nuevo_rect = pygame.Rect(self.x + dx, self.y + dy, 40, 40)
                if not self.colision_mapa(nuevo_rect):
                    self.x += dx
                    self.y += dy
                    print(f"Moving to: ({self.x}, {self.y})")  # Debug print
                    
                    if abs(self.x - target_x) < self.velocidad and abs(self.y - target_y) < self.velocidad:
                        self.path.pop(0)
                else:
                    self.path = None  # Recalculate path if blocked

        return True

    def colision_mapa(self, nuevo_rect):
        # Verificar colisiones con los bloques del mapa
        for bloque in self.mapa.obtener_rectangulos():
            if nuevo_rect.colliderect(bloque):
                return True
        return False

    def atacar(self):
        if self.objetivo:
            distancia = ((self.x - self.objetivo.x) ** 2 + (self.y - self.objetivo.y) ** 2) ** 0.5
            if distancia < 50:  # Solo atacar si está muy cerca
                print(f"¡Zombie atacando! Posición zombie: ({int(self.x)}, {int(self.y)}) -> Jugador: ({int(self.objetivo.x)}, {int(self.objetivo.y)})")
                # Aquí puedes agregar lógica de daño al jugador si lo deseas
                return True
            else:
                return False
        return False

    def actualizar_animacion(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:  # Ajusta este valor para cambiar la velocidad de animación
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites[self.current_animation])
            self.animation_timer = 0

    def dibujar_ruta(self, pantalla):
        if self.path and len(self.path) > 1:
            # Convertir los puntos de la ruta a coordenadas de pantalla
            puntos = [(p[0] * 50 + 25, p[1] * 50 + 25) for p in self.path]
            # Dibujar una línea que conecta todos los puntos de la ruta
            pygame.draw.lines(pantalla, (255, 0, 0), False, puntos, 2)

    def spawn(self, pantalla):
        # Primero dibujamos la ruta
        self.dibujar_ruta(pantalla)
        # Luego dibujamos el sprite como antes
        sprite = self.sprites[self.current_animation][self.current_sprite]
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)
        pantalla.blit(sprite, (self.x, self.y))
        self.actualizar_animacion()

    def actualizar(self):
        self.comportamiento.run()
