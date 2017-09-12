from pythonDesignPatterns.src.factory.pizzas.PizzaStore import PizzaStore
from pythonDesignPatterns.src.factory.pizzas.SimplePizzaFactory import SimplePizzaFactory

class PizzaTestDrive(object):
    @staticmethod
    def main():
        factory = SimplePizzaFactory()
        store = PizzaStore(factory)

        pizza = store.orderPizza("cheese")
        print("We ordered a " + pizza.name + "\n")

        pizza = store.orderPizza("veggie")
        print("We ordered a " + pizza.name + "\n")

if __name__ == '__main__':
    PizzaTestDrive.main()