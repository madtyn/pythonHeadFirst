from command.party.Hottub import Hottub
from command.party.Light import Light
from command.party.RemoteControl import RemoteControl
from command.party.Stereo import Stereo
from command.party.TV import TV
from command.party.Command import *


class RemoteLoader(object):
    @staticmethod
    def main():
        remoteControl = RemoteControl()

        light = Light("Living Room")
        tv = TV("Living Room")
        stereo = Stereo("Living Room")
        hottub = Hottub()

        lightOn = LightOnCommand(light)
        stereoOn = StereoOnCommand(stereo)
        tvOn = TVOnCommand(tv)
        hottubOn = HottubOnCommand(hottub)
        lightOff = LightOffCommand(light)
        stereoOff = StereoOffCommand(stereo)
        tvOff = TVOffCommand(tv)
        hottubOff = HottubOffCommand(hottub)

        partyOn = [ lightOn, stereoOn, tvOn, hottubOn ]
        partyOff = [ lightOff, stereoOff, tvOff, hottubOff ]

        partyOnMacro = MacroCommand(partyOn)
        partyOffMacro = MacroCommand(partyOff)

        remoteControl.setCommand(0, partyOnMacro, partyOffMacro)

        print(remoteControl)
        print("--- Pushing Macro On -= 1-")
        remoteControl.onButtonWasPushed(0)
        print("--- Pushing Macro Off -= 1-")
        remoteControl.offButtonWasPushed(0)


if __name__ == '__main__':
    RemoteLoader.main()
