from GameFrame import RoomObject, Globals
import pygame


class RedFlag(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        red_flag_image = self.load_image('flag_red.png')
        self.set_image(red_flag_image, 32, 32)

        self.handle_key_events = True

    def step(self):
        if self.x > Globals.SCREEN_WIDTH/2:
            Globals.winner = 'Red'
            self.room.running = False

    def key_pressed(self, key):
        if key[pygame.K_SPACE]:
            self.room.timed_out()
