# -*- coding: utf-8 -*-

# If the imports are from the same package, we can omit the package name, in this case 'strategy.'
from strategy.ducks import MallardDuck, ModelDuck, RubberDuck, DecoyDuck
from strategy.behaviors import FlyRocketPowered

if __name__ == '__main__':

    mallard = MallardDuck()
    rubberDuckie = RubberDuck()
    decoy = DecoyDuck()
    model = ModelDuck()


    mallard.performQuack()
    rubberDuckie.performQuack()
    decoy.performQuack()

    print

    model.performFly()
    model.flyBehavior = FlyRocketPowered()
    model.performFly()

