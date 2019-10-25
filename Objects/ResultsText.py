from GameFrame import TextObject
import pygame


class ResultsText(TextObject):
    def __init__(self, room, x, y, text='Not Set', size=60, font='Comic Sans MS', colour=(0, 0, 0), bold=False):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

        self.handle_key_events = True

        self.first_press = True
        self.end_time = False

    def key_pressed(self, key):
        if key[pygame.K_SPACE]:
            if self.first_press:
                self.first_press = False
                self.room.show_winner()
                self.set_timer(120, self.allow_close)
            if self.end_time:
                self.room.end_it()

    def allow_close(self):
        self.end_time = True
