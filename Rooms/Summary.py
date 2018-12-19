from GameFrame import Level, TextObject, Globals


class Summary(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = TextObject(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3, 'Turing Event', 80, 'Comic Sans MS', (255, 255, 255))
        self.add_room_object(title)

        ctf_text = TextObject(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3 * 2, 'Capture the Flag', 60, 'Comic Sans MS', (255, 255, 255))
        self.add_room_object(ctf_text)

        self.set_timer(150, self.start_battle)

    def start_battle(self):
        if Globals.current_battle < len(Globals.game_list):
            self.running = False
        else:
            self.running = False
            self.quitting = True
            Globals.exiting = True
