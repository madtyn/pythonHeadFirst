# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

'''
    The advantages of having an "interface" as FlyBehavior o QuackBehavior are:
    
        1.- The classes implementing (in Python would be inheriting) the "interface" share their source code for a behavior in a single piece of code
            When coming to changing some behavior, your change only affect the behavior and the classes using it. 
            The code is never written twice and the change is easy 
        2.- We can change AT RUNTIME the behavior of an instance
'''

class FlyBehavior():
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self):
        pass

class  FlyNoWay(FlyBehavior):
    def fly(self):
        print "I can't fly"

class  FlyRocketPowered(FlyBehavior):
    def fly(self):
        print 'I fly on a rocket'

class  FlyWithWings(FlyBehavior):
    def fly(self):
        print "I'm flying"

class QuackBehavior():
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print 'Quack'

class MuteQuack(QuackBehavior):
    def quack(self):
        print '...<quack intent...silence...>...'

class Squeak(QuackBehavior):
    def quack(self):
        print 'Squeak'

class FakeQuack(QuackBehavior):
    def quack(self):
        print 'Qwack'
