import os
import shutil
import subprocess
from GameFrame import Level, TextObject, Globals


class Battle(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = TextObject(self, 200, 200, 'Battle', 70, 'Comic Sans MS', (255, 255, 255))
        self.add_room_object(title)

        self.load_new_bots()

        self.set_timer(120, self.run_battle)

    def load_new_bots(self):
        index = Globals.current_battle
        for i in range(1, 6):
            source_path = os.path.join('Battles', 'Competitor_Files', Globals.game_list[index][0], 'Blue{}.py'.format(i))
            destination_path = os.path.join('Battles', 'Objects', 'Blue{}.py'.format(i))
            shutil.copy(source_path, destination_path)

            source_path = os.path.join('Battles', 'Competitor_Files', Globals.game_list[index][1], 'Red{}.py'.format(i))
            destination_path = os.path.join('Battles', 'Objects', 'Red{}.py'.format(i))
            shutil.copy(source_path, destination_path)

        Globals.current_battle += 1

    def run_battle(self):
        # Move to the Game Directory #
        os.chdir('Battles')
        subprocess.run(['python3', 'MainController.py'])
        os.chdir('..')
        self.running = False
