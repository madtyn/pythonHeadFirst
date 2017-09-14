class Waitress(object):
    allMenus = None

    def __init__(self, allMenus):
        super().__init__()
        self.allMenus = allMenus

    def printMenu(self):
        self.allMenus.print()

    def printVegetarianMenu(self):
        iterator = self.allMenus.createIterator()

        print("\nVEGETARIAN MENU\n -= 1--")
        while iterator.hasNext():
            menuComponent = iterator.getNext()
            try:
                if menuComponent.vegetarian:
                    menuComponent.print()

            except Exception as e:
                pass

