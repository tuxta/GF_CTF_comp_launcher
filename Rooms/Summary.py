from GameFrame import Level, TextObject, Globals


class Summary(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = TextObject(self, 200, 200, 'Results', 40, 'Comic Sans MS', (255, 255, 255))
        self.add_room_object(title)

        self.set_timer(150, self.start_battle)

    def start_battle(self):
        if Globals.current_battle < len(Globals.game_list):
            self.running = False
        else:
            self.running = False
            self.quitting = True
            Globals.exiting = True
