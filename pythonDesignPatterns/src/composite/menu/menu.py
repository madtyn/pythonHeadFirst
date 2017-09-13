from abc import ABCMeta


class MenuComponent(metaclass=ABCMeta):
    def add(self, menuComponent):
        return NotImplemented

    def remove(self, menuComponent):
        return NotImplemented

    def getChild(self, i):
        return NotImplemented

    def getName(self):
        return NotImplemented

    def getDescription(self):
        return NotImplemented

    def getPrice(self):
        return NotImplemented

    def isVegetarian(self):
        return NotImplemented

    def print(self):
        return NotImplemented


class Menu(MenuComponent):
    def __init__(self, name, description):
        super().__init__()
        self.menuComponents = []
        self.name = name
        self.description = description

    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)

    def getChild(self, i):
        return self.menuComponents[i]

    def print(self):
        print("\n" + self.name,)
        print(", " + self.description)
        print("---------------------")

        iterator = iter(self.menuComponents)
        menuComponent = next(iterator, False)
        while (menuComponent):
            menuComponent.print()
            menuComponent = next(iterator, False)


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def print(self):
        print(" {}".format(self.name),)
        if self.vegetarian:
            print("(v)",)

        print(", {}".format(self.price))
        print(" -- " + self.description)

