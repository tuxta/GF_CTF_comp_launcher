from GameFrame import RoomObject


class SomaLogo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        soma_logo = self.load_image('soma.png')
        self.set_image(soma_logo, 390, 130)
