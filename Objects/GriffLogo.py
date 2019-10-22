from GameFrame import RoomObject


class GriffLogo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        griff_logo = self.load_image('griffith.png')
        self.set_image(griff_logo, 360, 155)
