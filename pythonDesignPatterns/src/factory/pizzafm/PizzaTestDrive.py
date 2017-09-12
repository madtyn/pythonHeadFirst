from pythonDesignPatterns.src.factory.pizzafm.pizzaStores import ChicagoPizzaStore, NYPizzaStore, DependentPizzaStore


class PizzaTestDrive(object):
    @staticmethod
    def main():
        nyStore = NYPizzaStore()
        chicagoStore = ChicagoPizzaStore()
        depStore = DependentPizzaStore()

        pizza = nyStore.orderPizza("cheese")
        print("Ethan ordered a " + pizza.name + "\n")

        pizza = chicagoStore.orderPizza("cheese")
        print("Joel ordered a " + pizza.name + "\n")

        pizza = nyStore.orderPizza("clam")
        print("Ethan ordered a " + pizza.name + "\n")

        pizza = chicagoStore.orderPizza("clam")
        print("Joel ordered a " + pizza.name + "\n")

        pizza = nyStore.orderPizza("pepperoni")
        print("Ethan ordered a " + pizza.name + "\n")

        pizza = chicagoStore.orderPizza("pepperoni")
        print("Joel ordered a " + pizza.name + "\n")

        pizza = nyStore.orderPizza("veggie")
        print("Ethan ordered a " + pizza.name + "\n")

        pizza = chicagoStore.orderPizza("veggie")
        print("Joel ordered a " + pizza.name + "\n")

        pizza = depStore.createPizza("NY","veggie")
        print("Jack lives in NY went outside to the pizza shop to eat a " + pizza.name)

        pizza = depStore.createPizza("Chicago", "cheese")
        print("Jack on his holidays went to Chicago to eat a " + pizza.name)

if __name__ == '__main__':
    PizzaTestDrive.main()