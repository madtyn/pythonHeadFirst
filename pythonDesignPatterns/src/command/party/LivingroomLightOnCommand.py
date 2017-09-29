#package headfirst.command.party;

class LivingroomLightOnCommand(Command):
    light = None


    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        light.on()

    def undo(self):
        light.off()

