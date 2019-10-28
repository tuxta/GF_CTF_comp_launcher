from GameFrame import Level, TextObject, Globals
from Objects import IBMLogo, GriffLogo, VarsityLogo, VarsityText


class Summary(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = VarsityText(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3, 'Varsity College - 2019 Finals', 80, 'Comic Sans MS', (255, 255, 255))
        title.x = Globals.SCREEN_WIDTH / 2 - title.width / 2
        self.add_room_object(title)

        ctf_text = TextObject(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3 * 2, 'Capture the Flag', 100, 'Comic Sans MS', (255, 255, 255))
        ctf_text.x = Globals.SCREEN_WIDTH / 2 - ctf_text.width / 2
        self.add_room_object(ctf_text)

        if not Globals.first_run:
            self.set_timer(60, self.start_battle)

        ibm_logo = IBMLogo(self, Globals.SCREEN_WIDTH / 2 + 220, 0)
        self.add_room_object(ibm_logo)

        varsity_logo = VarsityLogo(self, Globals.SCREEN_WIDTH / 2 - 130, 0)
        self.add_room_object(varsity_logo)

        griff_logo = GriffLogo(self, Globals.SCREEN_WIDTH / 2 - 580, 0)
        self.add_room_object(griff_logo)

    def start_battle(self):
        if Globals.current_battle < len(Globals.game_list):
            self.running = False
        else:
            Globals.next_level = 2
            self.running = False
