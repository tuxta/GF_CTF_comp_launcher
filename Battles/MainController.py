#!/usr/bin/python3

import sys
import pygame
from GameFrame import Globals

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)

pygame.display.set_caption(Globals.window_name)
window_size = (Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
# screen = pygame.display.set_mode(window_size,
#                                 pygame.DOUBLEBUF, 32)

screen = pygame.display.set_mode(window_size,
                                 pygame.FULLSCREEN)

Globals.next_level = Globals.start_level
levels = Globals.levels

Globals.red_player = 'Nerang'
Globals.blue_player = 'Varsity'
#Globals.red_player = sys.argv[1]
#Globals.blue_player = sys.argv[2]

print(Globals.blue_player)
print(Globals.red_player)

# - Main Game Loop. Steps through the levels defined in levels[] - #
while Globals.running:

    curr_level = Globals.next_level
    Globals.next_level += 1
    Globals.next_level %= len(levels)
    mod_name = "Rooms.{}".format(levels[curr_level])
    mod = __import__(mod_name)
    class_name = getattr(mod, levels[curr_level])
    room = class_name(screen)
    exit_val = room.run()

    if exit_val is True or Globals.running is False:

        Globals.next_level = Globals.end_game_level

        if len(levels) == 1:
            break

    if Globals.exiting:
        break

sys.exit()
