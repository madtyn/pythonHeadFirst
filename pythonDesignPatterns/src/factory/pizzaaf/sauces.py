from abc import ABCMeta

# Could be _Sauce, so it would be not exported,
# or we could create an __all__ list with all exportable names

class Sauce(metaclass=ABCMeta):
    def __str__(self):
        pass


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"

