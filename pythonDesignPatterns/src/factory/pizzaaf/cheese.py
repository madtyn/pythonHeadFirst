from abc import ABCMeta

# Could be _Cheese, so it would be not exported,
# or we could create an __all__ list with all exportable names
class Cheese(metaclass=ABCMeta):
    def __str__(self):
        pass


class MozzarellaCheese(Cheese):

    def __str__(self):
        return "Shredded Mozzarella"


class ParmesanCheese(Cheese):

    def __str__(self):
        return "Shredded Parmesan"


class ReggianoCheese(Cheese):

    def __str__(self):
        return "Reggiano Cheese"

