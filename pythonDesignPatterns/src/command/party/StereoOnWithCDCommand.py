#package headfirst.command.party;

class StereoOnWithCDCommand(Command):
    stereo = None


    def __init__(self, stereo):
        super().__init__()
        self.stereo = stereo

    def execute(self):
        stereo.on()
        stereo.setCD()
        stereo.setVolume(11)

    def undo(self):
        stereo.off()

