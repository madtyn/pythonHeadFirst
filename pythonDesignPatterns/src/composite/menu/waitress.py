class Waitress(object):
    def __init__(self, allMenus):
        super().__init__()
        self.allMenus = allMenus

    def printMenu(self):
        self.allMenus.print()

