from abc import ABCMeta, abstractmethod
from pythonDesignPatterns.src.composite.menuiterator.iterator import NullIterator, CompositeIterator, Iterator


class MenuComponent(metaclass=ABCMeta):
    """
    A class which allowes to contain another instances of the same class
    """

    def add(self, menuComponent):
        """
        Adds a menuComponent instance to this menuComponent
        :param menuComponent: the menuComponent instance to add
        :return: not implemented, must be overriden, should be None or a boolean
        """
        return NotImplemented

    def remove(self, menuComponent):
        """

        :param menuComponent: the menuComponent instance to remove
        :return: not implemented, must be overriden, it should return the removed element
        """
        return NotImplemented

    def getChild(self, i):
        """
        Retrieves the i-th menuComponent contained within this class
        :param i: the index where the retrieved element is
        :return: the i-th child element
        """
        return NotImplemented

    @abstractmethod
    def createIterator(self):
        pass

    def print(self):
        return NotImplemented


class Menu(MenuComponent):
    """
    A concrete instantiation of MenuComponent, which can hold other MenuComponent instances
    as instance of Menu itself and MenuItem
    """
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.menuComponents = []

    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)

    def getChild(self, i):
        return self.menuComponents[i]

    def createIterator(self):
        return CompositeIterator(Iterator.createIterator(self.menuComponents))

    def print(self):
        print("\n{}".format(self.name),)
        print(", {}".format(self.description))
        print("---------------------")

        iterator = Iterator.createIterator(self.menuComponents)
        while iterator.hasNext():
            menuComponent = iterator.getNext()
            menuComponent.print()


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def createIterator(self):
        return NullIterator()

    def print(self):
        print(" {}".format(self.name),)
        if self.vegetarian:
            print("(v)",)

        print(", {}".format(self.price))
        print(" -- {}".format(self.description))

#vv MenuItemCompositeV2Main

#^^ MenuItemCompositeV2Main
#^^ MenuItemCompositeV2
