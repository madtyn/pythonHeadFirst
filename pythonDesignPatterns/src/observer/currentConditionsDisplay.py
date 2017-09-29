from observer.interfaces import Observer, DisplayElement

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        '''
        Constructor
        '''
        self.temperature = None
        self.humidity = None
        self.weatherData = weatherData;
        weatherData.registerObserver(self);


    def update(self, temperature, humidity, pressure):
        '''
            Updates this instance's values and displays this element's info
        '''
        self.temperature = temperature;
        self.humidity = humidity;
        self.display();

    def display(self):
        '''
        Displays this element's info
        '''
        print("Current conditions: %f F degrees and %f %% humidity" % (self.temperature, self.humidity))