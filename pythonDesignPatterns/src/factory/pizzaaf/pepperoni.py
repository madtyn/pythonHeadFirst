from abc import ABCMeta

# Could be _Pepperoni, so it would be not exported,
# or we could create an __all__ list with all exportable names
class Pepperoni(metaclass=ABCMeta):
    def __str__(self):
        pass


class SlicedPepperoni(Pepperoni):

    def __str__(self):
        return "Sliced Pepperoni"

