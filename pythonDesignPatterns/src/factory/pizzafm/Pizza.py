from abc import ABCMeta

class Pizza(metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()
        self.toppings = []

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for i in range(len(self.toppings)):
            print(" " + self.toppings[i])

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def __str__(self):
        display = ''
        display.append("---- " + self.name + " ----\n")
        display.append(self.dough + "\n")
        display.append(self.sauce + "\n")
        for i in range(len(self.toppings)):
            display.append(self.toppings.get[i] + "\n")

        return str(display)