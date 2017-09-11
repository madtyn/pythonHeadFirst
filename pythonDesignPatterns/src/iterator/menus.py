from abc import ABCMeta, abstractmethod
from iterators import DinerMenuIterator

class Menu():
    __metaclass__ = ABCMeta

    @abstractmethod
    def createIterator(self):
        pass

class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def isVegetarian(self):
        return self.vegetarian

class CafeMenu(Menu):

    def __init__(self):
        self.menuItems = {}
        self.addItem("Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True, 3.99)
        self.addItem("Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False, 3.69)
        self.addItem("Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True, 4.29)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems[menuItem.name] = menuItem

    def getItems(self):
        return self.menuItems

    def createIterator(self):
        return self.menuItems.values(self).iterator(self)


class DinerMenu(Menu):
    def __init__(self):
        self.MAX_ITEMS = 6
        self.numberOfItems = 0
        self.menuItems = [None for x in range(self.MAX_ITEMS)]  # This was intended to be a fixed-size array, MenuItem[MAX_ITEMS]

        self.addItem("Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT",
            "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day",
            "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog",
            "A hot dog, with saurkraut, relish, onions, topped with cheese",
            False, 3.05)
        self.addItem("Steamed Veggies and Brown Rice",
            "A medly of steamed vegetables over brown rice", True, 3.99)
        self.addItem("Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True, 3.89)


    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        if self.numberOfItems >= self.MAX_ITEMS:
            print "Sorry, menu is full!  Can't add item to menu"
        else:
            self.menuItems[self.numberOfItems] = menuItem
            self.numberOfItems = self.numberOfItems + 1



    def getMenuItems(self):
        return self.menuItems

    def createIterator(self):
        return DinerMenuIterator(self.menuItems)
        # return  AlternatingDinerMenuIterator(menuItems)


    # other menu methods here

class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menuItems = []

        self.addItem("K&B's Pancake Breakfast",
            "Pancakes with scrambled eggs, and toast",
            True,
            2.99)

        self.addItem("Regular Pancake Breakfast",
            "Pancakes with fried eggs, sausage",
            False,
            2.99)

        self.addItem("Blueberry Pancakes",
            "Pancakes made with fresh blueberries, and blueberry syrup",
            True,
            3.49)

        self.addItem("Waffles",
            "Waffles, with your choice of blueberries or strawberries",
            True,
            3.59)


    def addItem(self, name, description,
                        vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)


    def getMenuItems(self):
        return self.menuItems


    def createIterator(self):
        return self.menuItems.iterator()


    # other menu methods here
