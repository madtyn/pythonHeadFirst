from pythonDesignPatterns.src.factory.pizzaaf.pepperoni import SlicedPepperoni
from pythonDesignPatterns.src.factory.pizzaaf.clams import FrozenClams, FreshClams
from pythonDesignPatterns.src.factory.pizzaaf.doughs import ThickCrustDough,ThinCrustDough
from pythonDesignPatterns.src.factory.pizzaaf.sauces import PlumTomatoSauce, MarinaraSauce
from pythonDesignPatterns.src.factory.pizzaaf.cheese import MozzarellaCheese, ReggianoCheese
from pythonDesignPatterns.src.factory.pizzaaf.veggies import BlackOlives, Eggplant, Garlic, Mushroom, Onion, RedPepper, Spinach


class PizzaIngredientFactory():

    def createDough(self):
        pass
    def createSauce(self):
        pass
    def createCheese(self):
        pass
    def createVeggies(self):
        pass
    def createPepperoni(self):
        pass
    def createClam(self):
        pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThickCrustDough()

    def createSauce(self):
        return PlumTomatoSauce()

    def createCheese(self):
        return MozzarellaCheese()

    def createVeggies(self):
        veggies = [ BlackOlives(), Spinach(), Eggplant()]

        return veggies


def createPepperoni(self):
    return SlicedPepperoni()


def createClam(self):
    return FrozenClams()


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return ReggianoCheese()

    def createVeggies(self):
        veggies = [ Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FreshClams()

