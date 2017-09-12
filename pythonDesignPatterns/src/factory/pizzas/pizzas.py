from abc import ABCMeta


class Pizza(metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()
        self.toppings = []

    def prepare(self):
        print("Preparing " + self.name)

    def bake(self):
        print("Baking " + self.name)

    def cut(self):
        print("Cutting " + self.name)

    def box(self):
        print("Boxing " + self.name)

    def __str__(self):
        # code to display pizza name and ingredients
        display = ''
        display += "---- " + self.name + " ----\n"
        display += self.dough + "\n"
        display += self.sauce + "\n"
        for i in range(len(self.toppings)):
            display.append(self.toppings[i] + "\n")

        return str(display)


class CheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")


class ClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin crust"
        self.sauce = "White garlic sauce"
        self.toppings.add("Clams")
        self.toppings.add("Grated parmesan cheese")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.add("Sliced Pepperoni")
        self.toppings.add("Sliced Onion")
        self.toppings.add("Grated parmesan cheese")

class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.append("Shredded mozzarella")
        self.toppings.append("Grated parmesan")
        self.toppings.append("Diced onion")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")