'''
Created on 24/2/2016

@author: madtyn
'''

from decorator.beverages import Beverage
from abc import ABCMeta, abstractmethod

class CondimentDecorator(Beverage):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta

    def __init__(self, beverage):
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        pass

class Milk(CondimentDecorator) :
    def get_description(self) :
        return self.beverage.get_description() + ", Milk"


    def cost(self) :
        return .10 + self.beverage.cost()

class Mocha(CondimentDecorator) :
    def get_description(self) :
        return self.beverage.get_description() + ", Mocha"

    def cost(self) :
        return .20 + self.beverage.cost()

class Soy(CondimentDecorator) :
    def get_description(self) :
        return self.beverage.get_description() + ", Soy"

    def cost(self) :
        return .15 + self.beverage.cost()

class Whip(CondimentDecorator):
    def get_description(self) :
        return self.beverage.get_description() + ", Whip"

    def cost(self) :
        return .10 + self.beverage.cost()
