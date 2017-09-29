'''
Created on 19/12/2015

@author: madtyn
'''
from observer.interfaces import DisplayElement, Observer

class StatisticsDisplay(Observer, DisplayElement):
    '''
    DisplayElement which displays the statistics about temperature
    '''


    def __init__(self, weatherData):
        '''
        Constructor
        '''
        self.weatherData = weatherData
        self.maxTemp = 0.0
        self.minTemp = 200
        self.tempSum = 0.0
        self.numReadings = 0
        self.weatherData.registerObserver(self)

    def update(self, temp, humidity, pressure):
        '''
            Updates this instance's values and displays this element's info
        '''
        self.tempSum += temp
        self.numReadings += 1

        if (temp > self.maxTemp):
            self.maxTemp = temp


        if (temp < self.minTemp):
            self.minTemp = temp


        self.display()


    def display(self):
        '''
        Displays this element's info
        '''
        print("Avg/Max/Min temperature = " + str(self.tempSum / self.numReadings) + "/" + str(self.maxTemp) + "/" + str(self.minTemp))

