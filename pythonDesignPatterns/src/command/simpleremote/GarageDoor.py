#package headfirst.command.simpleremote;

class GarageDoor(object):


    def __init__(self):
        super().__init__()

    def up(self):
        print("Garage Door is Open")

    def down(self):
        print("Garage Door is Closed")

    def stop(self):
        print("Garage Door is Stopped")

    def lightOn(self):
        print("Garage light is on")

    def lightOff(self):
        print("Garage light is off")

