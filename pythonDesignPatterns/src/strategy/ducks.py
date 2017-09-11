# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from behaviors import FlyNoWay, FlyRocketPowered, FlyWithWings
from behaviors import MuteQuack, Squeak, FakeQuack, Quack

class Duck():
    '''
    This is the class using the FlyBehavior and QuackBehavior "interfaces", 
    also called Context in the definition of the pattern
    
    We could have defined the behavior as a @property but we wouldn't have taken no advantage of it
    '''

    # Makes an abstract class.
    # An alternative way would be declaring: class Duck(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, flyBehavior=None, quackBehavior=None):
        '''
        Constructor
        '''
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print 'All ducks can swim'


class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()

    def display(self):
        print "I'm a model duck"

class MallardDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        print "I'm a Mallard duck"

class RubberDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Squeak()

    def display(self):
        print "I'm a rubber duck"

class DecoyDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = MuteQuack()

    def display(self):
        print "I'm a decoy duck"

class RedHeadDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        print "I'm a real red headed duck"
