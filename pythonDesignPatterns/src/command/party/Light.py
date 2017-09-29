class Light(object):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.level = None

    def on(self):
        level = 100
        print("Light is on")

    def off(self):
        level = 0
        print("Light is off")

    def dim(self, level):
        self.level = level
        if level == 0:
            self.off()

        else:
            print("Light is dimmed to {}%".format(level))
