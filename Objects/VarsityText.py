from GameFrame import TextObject, Globals
import pygame


class VarsityText(TextObject):
    def __init__(self, room, x, y, text='Not Set', size=60, font='Comic Sans MS', colour=(0, 0, 0), bold=False):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_SPACE]:
            if Globals.first_run:
                Globals.first_run = False
                self.room.start_battle()

