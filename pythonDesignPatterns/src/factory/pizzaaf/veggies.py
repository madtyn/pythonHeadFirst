from abc import ABCMeta

# Could be _Veggies, so it would be not exported,
# or we could create an __all__ list with all exportable names
class Veggies(metaclass=ABCMeta):
    def __str__(self):
        pass


class Spinach(Veggies):
    def __str__(self):
        return "Spinach"


class Mushroom(Veggies):

    def __str__(self):
        return "Mushrooms"


class Onion(Veggies):
    def __str__(self):
        return "Onion"



class BlackOlives(Veggies):
    def __str__(self):
        return "Black Olives"

class RedPepper(Veggies):
    def __str__(self):
        return "Red Pepper"


class Garlic(Veggies):
    def __str__(self):
        return "Garlic"


class Eggplant(Veggies):
    def __str__(self):
        return "Eggplant"

