from GameFrame import Level, TextObject, Globals


class Summary(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = TextObject(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3, 'Varsity College - 2019 Semester 1', 80, 'Comic Sans MS', (255, 255, 255))
        title.x = Globals.SCREEN_WIDTH / 2 - title.width / 2
        self.add_room_object(title)

        ctf_text = TextObject(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3 * 2, 'Capture the Flag', 100, 'Comic Sans MS', (255, 255, 255))
        ctf_text.x = Globals.SCREEN_WIDTH / 2 - ctf_text.width / 2
        self.add_room_object(ctf_text)

        self.set_timer(150, self.start_battle)

    def start_battle(self):
        if Globals.current_battle < len(Globals.game_list):
            self.running = False
        else:
            self.running = False
            self.quitting = True
            Globals.exiting = True
