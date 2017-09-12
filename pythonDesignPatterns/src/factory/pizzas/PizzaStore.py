class PizzaStore(object):
    def __init__(self, factory):
        self.factory = factory

    def orderPizza(self, type):
        pizza = None

        pizza = self.factory.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza