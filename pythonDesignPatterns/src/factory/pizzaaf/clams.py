from abc import ABCMeta

# Could be _Clams, so it would be not exported,
# or we could create an __all__ list with all exportable names
class Clams(metaclass=ABCMeta):
    def __str__(self):
        pass


class FreshClams(Clams):

    def __str__(self):
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):

    def __str__(self):
        return "Frozen Clams from Chesapeake Bay"

