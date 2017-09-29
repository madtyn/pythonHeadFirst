#package headfirst.command.party;

class LivingroomLightOffCommand(Command):
    light = None


    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        light.off()

    def undo(self):
        light.on()

