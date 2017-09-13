from abc import ABCMeta

# Could be _Dough, so it would be not exported,
# or we could create an __all__ list with all exportable names
class Dough(metaclass=ABCMeta):
    def __str__(self):
        pass


class ThickCrustDough(Dough):
    def __str__(self):
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"

