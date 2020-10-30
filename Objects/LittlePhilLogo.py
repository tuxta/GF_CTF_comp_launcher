from GameFrame import RoomObject


class LittlePhilLogo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        ibm_logo = self.load_image('little-phil.png')
        self.set_image(ibm_logo, 460, 140)
