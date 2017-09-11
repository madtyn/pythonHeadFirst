'''
Created on 27/2/2016

@author: madtyn
'''

'''

'''


class State:
    def insertQuarter(self):
        pass
    def ejectQuarter(self):
        pass
    def turnCrank(self):
        pass
    def dispense(self):
        pass


class HasQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine


    def insertQuarter(self):
        print "You can't insert another quarter"


    def ejectQuarter(self):
        print "Quarter returned"
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())


    def turnCrank(self):
        print "You turned..."

        from random import randint
        winner = randint(0, 9)
        if ((winner == 0) and (self.gumballMachine.getCount() > 1)):
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print "No gumball dispensed"


    def __str__(self):
        return "waiting for turn of crank"


class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine


    def insertQuarter(self):
        print "You inserted a quarter"
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())


    def ejectQuarter(self):
        print "You haven't inserted a quarter"


    def turnCrank(self):
        print "You turned, but there's no quarter"


    def dispense(self):
        print "You need to pay first"


    def __str__(self):
        return "waiting for quarter"


class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine


    def insertQuarter(self):
        print "You can't insert a quarter, the machine is sold out"


    def ejectQuarter(self):
        print "You can't eject, you haven't inserted a quarter yet"


    def turnCrank(self):
        print "You turned, but there are no gumballs"


    def dispense(self):
        print "No gumball dispensed"


    def __str__(self):
        return "sold out"

class SoldState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine


    def insertQuarter(self):
        print "Please wait, we're already giving you a gumball"


    def ejectQuarter(self):
        print "Sorry, you already turned the crank"


    def turnCrank(self):
        print "Turning twice doesn't get you another gumball!"


    def dispense(self):
        self.gumballMachine.releaseBall()
        if (self.gumballMachine.getCount() > 0):
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print "Oops, out of gumballs!"
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())



    def __str__(self):
        return "dispensing a gumball"


class WinnerState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine


    def insertQuarter(self):
        print "Please wait, we're already giving you a Gumball"


    def ejectQuarter(self):
        print "Please wait, we're already giving you a Gumball"


    def turnCrank(self):
        print "Turning again doesn't get you another gumball!"


    def dispense(self):
        print "YOU'RE A WINNER! You get two gumballs for your quarter"
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print "Oops, out of gumballs!"
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def __str__(self):
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"
