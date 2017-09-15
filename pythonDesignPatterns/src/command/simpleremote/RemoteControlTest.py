from command.simpleremote.GarageDoor import GarageDoor
from command.simpleremote.GarageDoorOpenCommand import GarageDoorOpenCommand
from command.simpleremote.Light import Light
from command.simpleremote.LightOnCommand import LightOnCommand
from command.simpleremote.SimpleRemoteControl import SimpleRemoteControl


class RemoteControlTest(object):
    @staticmethod
    def main():
        remote = SimpleRemoteControl()
        light = Light()
        garageDoor = GarageDoor()
        lightOn = LightOnCommand(light)
        garageOpen = GarageDoorOpenCommand(garageDoor)
        remote.setCommand(lightOn)
        remote.buttonWasPressed()
        remote.setCommand(garageOpen)
        remote.buttonWasPressed()


if __name__ == '__main__':
    RemoteControlTest.main()
