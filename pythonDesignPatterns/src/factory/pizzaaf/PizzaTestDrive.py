import os

from pythonDesignPatterns.src.factory.pizzaaf.PizzaStore import NYPizzaStore, ChicagoPizzaStore

class PizzaTestDrive(object):
    @staticmethod
    def main():
        nyStore = NYPizzaStore()
        chicagoStore = ChicagoPizzaStore()

        pizza = nyStore.orderPizza("cheese")
        print("Ethan ordered a {}".format(pizza) + os.linesep)

        pizza = chicagoStore.orderPizza("cheese")
        print("Joel ordered a {}".format(pizza) + os.linesep)

        pizza = nyStore.orderPizza("clam")
        print("Ethan ordered a {}".format(pizza) + os.linesep)

        pizza = chicagoStore.orderPizza("clam")
        print("Joel ordered a {}".format(pizza) + os.linesep)

        pizza = nyStore.orderPizza("pepperoni")
        print("Ethan ordered a {}".format(pizza) + os.linesep)

        pizza = chicagoStore.orderPizza("pepperoni")
        print("Joel ordered a {}".format(pizza) + os.linesep)

        pizza = nyStore.orderPizza("veggie")
        print("Ethan ordered a {}".format(pizza) + os.linesep)

        pizza = chicagoStore.orderPizza("veggie")
        print("Joel ordered a {}".format(pizza) + os.linesep)

if __name__ == '__main__':
    PizzaTestDrive.main()