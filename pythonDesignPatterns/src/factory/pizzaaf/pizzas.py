from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def __str__(self):
        result = ''
        result += "---- " + self.name + " ----\n"
        if self.dough:
            result += self.dough
            result += "\n"

        if self.sauce:
            result += self.sauce
            result += "\n"

        if self.cheese:
            result += self.cheese
            result += "\n"

        if self.veggies and len(self.veggies):
            result += ", ".join(self.veggies)
            result += "\n"

        if self.clam:
            result += self.clam
            result += "\n"

        if self.pepperoni:
            result += self.pepperoni
            result += "\n"

        return str(result)



class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing " + self.name)
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.createCheese()


class ClamPizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing " + self.name)
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.createCheese()
        clam = self.ingredientFactory.createClam()


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing " + self.name)
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.createCheese()
        veggies = self.ingredientFactory.createVeggies()
        pepperoni = self.ingredientFactory.createPepperoni()



class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing " + self.name)
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.createCheese()
        veggies = self.ingredientFactory.createVeggies()

