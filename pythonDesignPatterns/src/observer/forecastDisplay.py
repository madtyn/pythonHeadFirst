from interfaces import Observer, DisplayElement

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weatherData) :
        '''
        Constructor
        '''
        self.currentPressure = float(29.92)
        self.lastPressure = None
        self.weatherData = weatherData
        weatherData.registerObserver(self)


    def update(self, temp, humidity, pressure):
        '''
            Updates this instance's values and displays this element's info
        '''
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure

        self.display();


    def display(self) :
        '''
        Displays this element's info
        '''
        print("Forecast: ",)
        if (self.currentPressure > self.lastPressure):
            print("Improving weather on the way!")
        elif (self.currentPressure == self.lastPressure):
            print("More of the same")
        elif (self.currentPressure < self.lastPressure):
            print("Watch out for cooler, rainy weather")



