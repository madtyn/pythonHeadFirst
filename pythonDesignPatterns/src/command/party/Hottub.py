class Hottub(object):
    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.isOn = None

    def on(self):
        self.isOn = True

    def off(self):
        self.isOn = False

    def circulate(self):
        if self.isOn:
            print("Hottub is bubbling!")

    def jetsOn(self):
        if self.isOn:
            print("Hottub jets are on")

    def jetsOff(self):
        if self.isOn:
            print("Hottub jets are off")

    def setTemperature(self, temperature):
        if temperature > self.temperature:
            print("Hottub is heating to a steaming {} degrees".format(temperature))

        else:
            print("Hottub is cooling to {} degrees".format(temperature))

        self.temperature = temperature

