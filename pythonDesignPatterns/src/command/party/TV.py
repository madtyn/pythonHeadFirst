class TV(object):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.channel = None

    def on(self):
        print(self.location + " TV is on")

    def off(self):
        print(self.location + " TV is off")

    def setInputChannel(self):
        self.channel = 3
        print(self.location + " TV channel is set for DVD")

