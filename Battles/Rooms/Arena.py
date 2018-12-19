from GameFrame import Level, Globals, RedFlag, BlueFlag
from Objects import Red1, Red2, Red3, Red4, Red5
from Objects import Blue1, Blue2, Blue3, Blue4, Blue5


class Arena(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image("background.png")

        Globals.red_flag = RedFlag(self, 50, Globals.SCREEN_HEIGHT / 2 - 26)
        Globals.blue_flag = BlueFlag(self, Globals.SCREEN_WIDTH - 82, Globals.SCREEN_HEIGHT / 2 - 26)

        self.add_room_object(Globals.red_flag)
        self.add_room_object(Globals.blue_flag)

        Globals.red_bots.append(Red1(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4))
        Globals.blue_bots.append(Blue1(self, 108, Globals.SCREEN_HEIGHT / 3))
        Globals.red_bots.append(Red2(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4 * 2))
        Globals.blue_bots.append(Blue2(self, 108, Globals.SCREEN_HEIGHT / 3 * 2))
        Globals.red_bots.append(Red3(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4 * 3))
        Globals.blue_bots.append(Blue3(self, 228, Globals.SCREEN_HEIGHT / 4))
        Globals.red_bots.append(Red4(self, Globals.SCREEN_WIDTH - 140, Globals.SCREEN_HEIGHT / 3))
        Globals.blue_bots.append(Blue4(self, 228, Globals.SCREEN_HEIGHT / 4 * 2))
        Globals.red_bots.append(Red5(self, Globals.SCREEN_WIDTH - 140, Globals.SCREEN_HEIGHT / 3 * 2))
        Globals.blue_bots.append(Blue5(self, 228, Globals.SCREEN_HEIGHT / 4 * 3))

        for i in range(len(Globals.red_bots)):
            self.add_room_object(Globals.red_bots[i])

        for i in range(len(Globals.blue_bots)):
            self.add_room_object(Globals.blue_bots[i])
            Globals.blue_bots[i].rotate(180)

        Globals.background_music = self.load_sound('battle-music.ogg')
        Globals.background_music.play(-1)

