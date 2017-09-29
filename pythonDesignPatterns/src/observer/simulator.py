# -*- coding: utf-8 -*-

# If the imports are from the same package, we can omit the package name, in this case 'observer.'
from observer.weatherData import WeatherData
from observer.currentConditionsDisplay import CurrentConditionsDisplay
from observer.forecastDisplay import ForecastDisplay
from observer.statisticsDisplay import StatisticsDisplay


if __name__ == '__main__':
    # We make an instance of the data source
    weatherData = WeatherData()

    # We create instances of descendents from Observer which, at the same time, can display data (DisplayElement)
    currentDisplay = CurrentConditionsDisplay(weatherData)
    statisticsDisplay = StatisticsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)

    print()

    # When the measurements of the weatherData change, the observers get notified and print the data
    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)


