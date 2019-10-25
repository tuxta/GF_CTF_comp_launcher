from GameFrame import Level, Globals, TextObject
from Objects import IBMLogo, GriffLogo, VarsityLogo, ResultsText
from collections import Counter
import os


class Result(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = ResultsText(self, Globals.SCREEN_WIDTH / 3, Globals.SCREEN_HEIGHT / 3, 'Results', 60, 'Comic Sans MS',
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

    def end_it(self):
        self.running = False
        self.quitting = True
        Globals.running = False

    def show_winner(self):
        file_name = os.path.join('Battles', 'results.txt')
        log_file = open(file_name, 'r')
        results_from_file = log_file.read().splitlines(False)
        log_file.close()

        ordered_results = list(Counter(results_from_file).most_common())

        y_pos = 320
        for team in ordered_results:
            team_result = TextObject(self, Globals.SCREEN_WIDTH / 3, y_pos, '{}    {}'.format(team[0], team[1]), 80,
                                     'Comic Sans MS',
                                     (255, 255, 255)
                                     )
            team_result.x = Globals.SCREEN_WIDTH / 2 - team_result.width / 2
            self.add_room_object(team_result)
            y_pos += 80
