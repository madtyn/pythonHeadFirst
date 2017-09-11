'''
Created on 23/2/2016

@author: madtyn
'''
from abc import ABCMeta, abstractmethod

class Beverage(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta


    def __init__(self, params):
        '''
        Constructor
        '''
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass

class DarkRoast(Beverage) :
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self) :
        return .99

class Decaf(Beverage) :
    def __init__(self):
        self.description = "Decaf Coffee"

    def cost(self) :
        return 1.05

class Espresso(Beverage) :
    def __init__(self):
        self.description = "Espresso"

    def cost(self) :
        return 1.99

class HouseBlend(Beverage) :
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self) :
        return .89
