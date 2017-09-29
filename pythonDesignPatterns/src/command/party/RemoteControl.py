#
# This is the invoker
#
from command.party.Command import NoCommand


class RemoteControl(object):
    def __init__(self):
        super().__init__()
        noCommand = NoCommand()

        self.onCommands = [noCommand]*7
        self.offCommands = [noCommand]*7
        self.undoCommand = noCommand

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPushed(self):
        self.undoCommand.undo()

    def __str__(self):
        stringBuff = ''
        stringBuff += "\n -= 1---- Remote Control -------\n"
        for i in range(len(self.onCommands)):
            stringBuff += "[slot " + str(i) + "] " + self.onCommands[i].__class__.__name__ \
                + " " + self.offCommands[i].__class__.__name__ + "\n"

        stringBuff += "[undo] " + self.undoCommand.__class__.__name__ + "\n"
        return stringBuff

