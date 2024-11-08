# main.py

import pygame
from entities.player.personaje import Agente
from map.mapa import Map
from entities.enemy.enemigo import Zombie
from scenes.menu_scene import mostrar_menu
from utils.constants import Constants
from utils.game_window import GameWindow

ventana = GameWindow.get_instance()

def main():
    mostrar_menu()

if __name__ == "__main__":
    main()
