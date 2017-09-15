#package headfirst.command.simpleremote;

#import java.util.*;

#
# This is the invoker
#
class SimpleRemoteControl(object):
    def __init__(self):
        super().__init__()
        self.slot = None

    def setCommand(self, command):
        self.slot = command

    def buttonWasPressed(self):
        self.slot.execute()

