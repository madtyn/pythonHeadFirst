from interfaces import Subject

class WeatherData(Subject):
    '''
    This is the data source and the subject being observed
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.observers = []  # Initially empty
        self.temperature = None
        self.humidity = None
        self.pressure = None


    def registerObserver(self, observer):
        '''
        Just adds the new observer to the end of the list
        '''
        self.observers.append(observer)


    def removeObserver(self, observer):
        '''
        Removes the observer from the list supposing there are no duplicates.
        So, we use remove for erasing the first ocurrence of the observer
        and do nothing on ValueError
        '''
        try:
            return self.observers.remove(observer)
        except ValueError:
            print 'Observer not found: ', str(observer)


    def notifyObservers(self):
        '''
        This tells all the observers the news. The observers have to implement update()
        '''
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        '''
        When the measurements change, we tell the observers
        '''
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        '''
        Updates the values and calls the method which notifies the observers
        '''
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()
