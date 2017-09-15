#package headfirst.command.simpleremote;
from command.simpleremote.Command import Command


class LightOnCommand(Command):
    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        self.light.on()

