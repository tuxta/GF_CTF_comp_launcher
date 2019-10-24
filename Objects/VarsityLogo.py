from GameFrame import RoomObject


class VarsityLogo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        varsity_logo = self.load_image('varsity.png')
        self.set_image(varsity_logo, 250, 150)
