from abc import ABCMeta, abstractmethod

from pythonDesignPatterns.src.factory.pizzaaf.PizzaIngredientFactory import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory
from pythonDesignPatterns.src.factory.pizzaaf.pizzas import *


class PizzaStore(metaclass=ABCMeta):
    @abstractmethod
    def _createPizza(self, item):
        pass

    def orderPizza(self, type):
        pizza = self._createPizza(type)
        print("--- Making a " + pizza.name + " ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def _createPizza(self, item):
        pizza = None
        ingredientFactory = ChicagoPizzaIngredientFactory()

        if item == "cheese":

            pizza = CheesePizza(ingredientFactory)
            pizza.name = "Chicago Style Cheese Pizza"

        elif item == "veggie":

            pizza = VeggiePizza(ingredientFactory)
            pizza.name = "Chicago Style Veggie Pizza"

        elif item == "clam":

            pizza = ClamPizza(ingredientFactory)
            pizza.name = "Chicago Style Clam Pizza"

        elif item == "pepperoni":

            pizza = PepperoniPizza(ingredientFactory)
            pizza.name = "Chicago Style Pepperoni Pizza"

        return pizza


class NYPizzaStore(PizzaStore):

    def _createPizza(self, item):
        pizza = None
        ingredientFactory = NYPizzaIngredientFactory()

        if item == "cheese":

            pizza = CheesePizza(ingredientFactory)
            pizza.name = "New York Style Cheese Pizza"

        elif item == "veggie":

            pizza = VeggiePizza(ingredientFactory)
            pizza.name = "New York Style Veggie Pizza"

        elif item == "clam":

            pizza = ClamPizza(ingredientFactory)
            pizza.name = "New York Style Clam Pizza"

        elif item == "pepperoni":

            pizza = PepperoniPizza(ingredientFactory)
            pizza.name = "New York Style Pepperoni Pizza"

        return pizza

