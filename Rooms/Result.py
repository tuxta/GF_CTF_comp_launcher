from GameFrame import Level, TextObject, Globals
from Objects import IBMLogo, GriffLogo, VarsityLogo


class Result(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = TextObject(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3, 'Results', 80, 'Comic Sans MS',
                           (255, 255, 255)
                           )
        title.x = Globals.SCREEN_WIDTH / 2 - title.width / 2
        self.add_room_object(title)

        ibm_logo = IBMLogo(self, Globals.SCREEN_WIDTH / 2 + 220, 0)
        self.add_room_object(ibm_logo)

        varsity_logo = VarsityLogo(self, Globals.SCREEN_WIDTH / 2 - 130, 0)
        self.add_room_object(varsity_logo)

        griff_logo = GriffLogo(self, Globals.SCREEN_WIDTH / 2 - 580, 0)
        self.add_room_object(griff_logo)
