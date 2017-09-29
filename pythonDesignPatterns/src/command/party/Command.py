from abc import abstractmethod

class Command():
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class HottubOnCommand(Command):
    def __init__(self, hottub):
        super().__init__()
        self.hottub = hottub

    def execute(self):
        self.hottub.on()
        self.hottub.setTemperature(104)
        self.hottub.circulate()

    def undo(self):
        self.hottub.off()

class HottubOffCommand(Command):
    def __init__(self, hottub):
        super().__init__()
        self.hottub = hottub

    def execute(self):
        self.hottub.setTemperature(98)
        self.hottub.off()

    def undo(self):
        self.hottub.on()

class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        super().__init__()
        self.ceilingFan = ceilingFan
        self.prevSpeed = None

    def execute(self):
        prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()

    def undo(self):
        self.ceilingFan.undo()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        super().__init__()
        self.ceilingFan = ceilingFan
        self.prevSpeed = None

    def execute(self):
        prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        self.ceilingFan.undo()

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        super().__init__()
        self.ceilingFan = ceilingFan
        self.prevSpeed = None

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()

    def undo(self):
        self.ceilingFan.undo()


class LightOffCommand(Command):
    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class LightOnCommand(Command):
    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class MacroCommand(Command):
    def __init__(self, commands):
        super().__init__()
        self.commands = commands

    def execute(self):
        for i in range(len(self.commands)):
            self.commands[i].execute()

    """
     NOTE: these commands have to be done backwards to ensure proper undo functionality
     """
    def undo(self):
        for i in range(len(self.commands)-1, -1, -1):
            self.commands[i].undo()

class NoCommand(Command):
    def execute(self):
        pass
    def undo(self):
        pass

class StereoOffCommand(Command):
    def __init__(self, stereo):
        super().__init__()
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()

class StereoOnCommand(Command):
    def __init__(self, stereo):
        super().__init__()
        self.stereo = stereo

    def execute(self):
        self.stereo.on()

    def undo(self):
        self.stereo.off()

class TVOnCommand(Command):
    def __init__(self, tv):
        super().__init__()
        self.tv= tv

    def execute(self):
        self.tv.on()
        self.tv.setInputChannel()

    def undo(self):
        self.tv.off()

class TVOffCommand(Command):
    def __init__(self, tv):
        super().__init__()
        self.tv= tv

    def execute(self):
        self.tv.off()

    def undo(self):
        self.tv.on()

