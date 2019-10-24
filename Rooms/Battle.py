import os
import pygame
import shutil
import subprocess
from GameFrame import Level, TextObject, Globals


class Battle(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.background_sound = self.load_sound('dramatic_event.ogg')
        self.background_sound.play()

        red_team = TextObject(self,
                              Globals.SCREEN_WIDTH / 4,
                              Globals.SCREEN_HEIGHT / 4,
                              'Red : {}'.format(Globals.game_list[Globals.current_battle][1]),
                              70,
                              'Comic Sans MS',
                              (255, 0, 0)
                              )
        red_team.x = Globals.SCREEN_WIDTH / 2 - red_team.width / 2
        self.add_room_object(red_team)

        versus = TextObject(self,
                            Globals.SCREEN_WIDTH / 3,
                            Globals.SCREEN_HEIGHT / 2,
                            'Versus',
                            70,
                            'Comic Sans MS',
                            (255, 255, 255)
                            )
        versus.x = Globals.SCREEN_WIDTH / 2 - versus.width / 2
        self.add_room_object(versus)

        blue_team = TextObject(self,
                               Globals.SCREEN_WIDTH / 4,
                               Globals.SCREEN_HEIGHT / 4 * 3,
                               'Blue : {}'.format(Globals.game_list[Globals.current_battle][0]),
                               70,
                               'Comic Sans MS',
                               (0, 0, 255)
                               )
        blue_team.x = Globals.SCREEN_WIDTH / 2 - blue_team.width / 2
        self.add_room_object(blue_team)

        self.load_new_bots()

        self.set_timer(200, self.run_battle)

    def load_new_bots(self):
        index = Globals.current_battle
        for i in range(1, 6):
            source_path = os.path.join('Battles', 'Competitor_Files', Globals.game_list[index][0], 'Blue{}.py'.format(i))
            destination_path = os.path.join('Battles', 'Objects', 'Blue{}.py'.format(i))
            shutil.copy(source_path, destination_path)

            source_path = os.path.join('Battles', 'Competitor_Files', Globals.game_list[index][1], 'Red{}.py'.format(i))
            destination_path = os.path.join('Battles', 'Objects', 'Red{}.py'.format(i))
            shutil.copy(source_path, destination_path)

    def run_battle(self):
        # Move to the Game Directory #
        self.background_sound.stop()
        os.chdir('Battles')
        pygame.display.toggle_fullscreen()
        subprocess.run(['python3', 'MainController.py',
                        Globals.game_list[Globals.current_battle][0],
                        Globals.game_list[Globals.current_battle][1]
                        ])
        os.chdir('..')
        pygame.display.toggle_fullscreen()
        Globals.current_battle += 1
        self.running = False
        self.quitting = True
