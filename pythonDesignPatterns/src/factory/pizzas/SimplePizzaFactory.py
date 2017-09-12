from pythonDesignPatterns.src.factory.pizzas.pizzas import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza

class SimplePizzaFactory(object):
    def createPizza(self, type):
        pizza = None

        if type == "cheese":
            pizza = CheesePizza()
        elif type == "pepperoni":
            pizza = PepperoniPizza()
        elif type == "clam":
            pizza = ClamPizza()
        elif type == "veggie":
            pizza = VeggiePizza()

        return pizza