from GameFrame import RoomObject


class IBMLogo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        ibm_logo = self.load_image('ibm.png')
        self.set_image(ibm_logo, 340, 148)
