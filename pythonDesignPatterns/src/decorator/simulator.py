'''
Created on 24/2/2016

@author: madtyn
'''
from decorator.beverages import DarkRoast, Espresso, HouseBlend  # , Decaf
from decorator.condimentDecorators import Milk, Mocha, Soy, Whip

if __name__ == '__main__':
    beverage = Espresso()
    print beverage.get_description() + " $" , beverage.cost()

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print beverage2.get_description() + " $", beverage2.cost()

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Milk(beverage3)
    beverage3 = Whip(beverage3)
    print beverage3.get_description() + " $", beverage3.cost()
