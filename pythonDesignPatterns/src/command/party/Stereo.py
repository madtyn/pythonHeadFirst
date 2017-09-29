class Stereo(object):
    def __init__(self, location):
        super().__init__()
        self.location = location

    def on(self):
        print(self.location + " stereo is on")

    def off(self):
        print(self.location + " stereo is off")

    def setCD(self):
        print(self.location + " stereo is set for CD input")

    def setDVD(self):
        print(self.location + " stereo is set for DVD input")

    def setRadio(self):
        print(self.location + " stereo is set for Radio")

    def setVolume(self, volume):
        # code to set the volume
        # valid range: 1-11 (after all 11 is better than 10, right?)
        print(self.location + " Stereo volume set to " + volume)

