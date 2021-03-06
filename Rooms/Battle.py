import os
import pygame
import shutil
import platform
import subprocess
from GameFrame import Level, TextObject, Globals
from Objects import IBMLogo, VarsityLogo, GriffLogo, SomaLogo, LittlePhilLogo


class Battle(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.background_sound = self.load_sound('dramatic_event.ogg')
        self.background_sound.play()

        ibm_logo = IBMLogo(self, Globals.SCREEN_WIDTH / 2 + 220, 0)
        self.add_room_object(ibm_logo)

        varsity_logo = VarsityLogo(self, Globals.SCREEN_WIDTH / 2 - 130, 0)
        self.add_room_object(varsity_logo)

        griff_logo = GriffLogo(self, Globals.SCREEN_WIDTH / 2 - 580, 0)
        self.add_room_object(griff_logo)

        soma_logo = SomaLogo(self, 80, Globals.SCREEN_HEIGHT - 140)
        self.add_room_object(soma_logo)

        little_phil_logo = LittlePhilLogo(
            self,
            Globals.SCREEN_WIDTH - 500,
            Globals.SCREEN_HEIGHT - 160
        )
        self.add_room_object(little_phil_logo)

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
                            Globals.SCREEN_HEIGHT / 2 - 70,
                            'Versus',
                            70,
                            'Comic Sans MS',
                            (255, 255, 255)
                            )
        versus.x = Globals.SCREEN_WIDTH / 2 - versus.width / 2
        self.add_room_object(versus)

        blue_team = TextObject(self,
                               Globals.SCREEN_WIDTH / 4,
                               Globals.SCREEN_HEIGHT / 4 * 3 - 140,
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
        if platform.system() == "Windows":
            subprocess.run(['py', 'MainController.py',
                            Globals.game_list[Globals.current_battle][0],
                            Globals.game_list[Globals.current_battle][1]
                            ])
        else:
            subprocess.run(['python3', 'MainController.py',
                            Globals.game_list[Globals.current_battle][0],
                            Globals.game_list[Globals.current_battle][1]
                            ])
        os.chdir('..')
        pygame.display.toggle_fullscreen()
        Globals.current_battle += 1
        self.running = False
        self.quitting = True
