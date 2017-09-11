class Iterator():
    def __init__(self):
        pass

    def hasNext(self):
        pass

    def next(self):
        pass

class DinerMenuIterator(Iterator):
    def __init__(self, list):
        self.list = []  # List of MenuItem
        self.position = 0

    def next(self):
        menuItem = list[self.position]
        self.position = self.position + 1
        return menuItem

    def hasNext(self):
        if self.position >= list.length or list[self.position] == None:
            return False
        else:
            return True

    def remove(self):
        if self.position <= 0:
            raise StandardError("You can't remove an item until you've done at least one next()")

        if list[self.position - 1] != None:
            for i in range(self.position - 1, len(list) - 1):
                list[i] = list[i + 1]

        list[-1] = None


from datetime import datetime

class AlternatingDinerMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        rightNow = datetime.now()
        self.position = rightNow.weekday() % 2

    def next(self):
        menuItem = self.items[self.position]
        self.position = self.position + 2
        return menuItem

    def hasNext(self):
        if (self.position >= self.items.length or self.items[self.position] == None):
            return False
        else:
            return True

    def remove(self):
        raise AttributeError(
            "Alternating Diner Menu Iterator does not support remove()")
