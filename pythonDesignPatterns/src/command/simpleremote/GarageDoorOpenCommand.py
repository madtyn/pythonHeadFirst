from command.simpleremote.Command import Command


class GarageDoorOpenCommand(Command):
    def __init__(self, garageDoor):
        super().__init__()
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.up()

