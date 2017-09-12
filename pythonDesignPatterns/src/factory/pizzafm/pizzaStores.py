from pythonDesignPatterns.src.factory.pizzafm.nyPizzas import *
from pythonDesignPatterns.src.factory.pizzafm.chPizzas import *

from abc import ABCMeta, abstractmethod


class DependentPizzaStore(object):
    def createPizza(self, style, type):
        pizza = None
        if style == "NY":
            if type == "cheese":
                pizza = NYStyleCheesePizza()
            elif type == "veggie":
                pizza = NYStyleVeggiePizza()
            elif type == "clam":
                pizza = NYStyleClamPizza()
            elif type == "pepperoni":
                pizza = NYStylePepperoniPizza()
        elif style == "Chicago":
            if type == "cheese":
                pizza = ChicagoStyleCheesePizza()
            elif type == "veggie":
                pizza = ChicagoStyleVeggiePizza()
            elif type == "clam":
                pizza = ChicagoStyleClamPizza()
            elif type == "pepperoni":
                pizza = ChicagoStylePepperoniPizza()

        else:
            print("Error: invalid type of pizza")
            return None

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class PizzaStore(metaclass=ABCMeta):
    @abstractmethod
    def createPizza(self, item):
        pass

    def orderPizza(self, type):
        pizza = self.createPizza(type)
        print("--- Making a " + pizza.name + " ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, item):
        if item == "cheese":
            return ChicagoStyleCheesePizza()
        elif item == "veggie":
            return ChicagoStyleVeggiePizza()
        elif item == "clam":
            return ChicagoStyleClamPizza()
        elif item == "pepperoni":
            return ChicagoStylePepperoniPizza()


class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        if item == "cheese":
            return NYStyleCheesePizza()
        elif item == "veggie":
            return NYStyleVeggiePizza()
        elif item == "clam":
            return NYStyleClamPizza()
        elif item == "pepperoni":
            return NYStylePepperoniPizza()

