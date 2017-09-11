# -*- coding: utf-8 -*-

# If the imports are from the same package, we can omit the package name, in this case 'strategy.'
from strategy.ducks import MallardDuck, ModelDuck
from strategy.behaviors import FlyRocketPowered

if __name__ == '__main__':

    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()

    print

    model = ModelDuck()
    model.display()
    model.performFly()
    model.flyBehavior = FlyRocketPowered()
    model.performFly()
