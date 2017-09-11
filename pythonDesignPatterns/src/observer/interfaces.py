# -*- coding: utf-8 -*-
'''
Created on 13/12/2015

@author: madtyn
'''

from abc import ABCMeta, abstractmethod

class Subject():
    __metaclass__ = ABCMeta

    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Observer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass

class DisplayElement():
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        pass
