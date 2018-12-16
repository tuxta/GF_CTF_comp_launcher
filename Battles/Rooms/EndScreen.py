from GameFrame import Level, TextObject, Globals


class EndScreen(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)
        winner = Globals.winner + ' Wins'
        winner_text = TextObject(self, 250, 250, winner, 80)
        winner_text.colour = (255, 255, 255)
        winner_text.update_text()
        self.add_room_object(winner_text)

        self.set_timer(120, self.end_game)

    def end_game(self):
        self.running = False
        self.quitting = True
        Globals.exiting = True
