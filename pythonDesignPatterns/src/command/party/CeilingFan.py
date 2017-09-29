
class CeilingFan(object):
    CeilingFan.HIGH = 3
    CeilingFan.MEDIUM = 2
    CeilingFan.LOW = 1
    CeilingFan.OFF = 0


    def __init__(self, location):
        super().__init__()
        self.location = location
        self.speed = None
        self.switch = {
            CeilingFan.HIGH: self.high,
            CeilingFan.MEDIUM: self.medium,
            CeilingFan.LOW: self.low,
        }

    def high(self):
        # turns the ceiling fan on to high
        speed = CeilingFan.HIGH
        print(self.location + " ceiling fan is on high")

    def medium(self):
        # turns the ceiling fan on to medium
        speed = CeilingFan.MEDIUM
        print(self.location + " ceiling fan is on medium")

    def low(self):
        # turns the ceiling fan on to low
        speed = CeilingFan.LOW
        print(self.location + " ceiling fan is on low")

    def off(self):
        # turns the ceiling fan off
        speed = CeilingFan.OFF
        print(self.location + " ceiling fan is off")

    def undo(self):
        func = self.switch.get(prevSpeed, self.off)
        func()

    def getSpeed(self):
        return self.speed

