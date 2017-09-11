'''
Created on 1/3/2016

@author: madtyn
'''
from states import HasQuarterState, NoQuarterState, SoldOutState, SoldState, WinnerState

class GumballMachine:
    def __init__(self, numberGumballs):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        self.count = 0

        self.count = numberGumballs
        self.state = None
        if (numberGumballs > 0):
            self.state = self.noQuarterState



    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state):
        self.state = state

    def releaseBall(self):
        print "A gumball comes rolling out the slot..."
        if (self.count != 0):
            self.count = self.count - 1

    def getCount(self):
        return self.count

    def refill(self, count):
        self.count = count
        self.state = self.noQuarterState

    def getState(self):
        return self.state


    def getSoldOutState(self):
        return self.soldOutState


    def getNoQuarterState(self):
        return self.noQuarterState


    def getHasQuarterState(self):
        return self.hasQuarterState


    def getSoldState(self):
        return self.soldState


    def getWinnerState(self):
        return self.winnerState


    def __str__(self):
        result = ''
        result += "\nMighty Gumball, Inc."
        result += "\nJava-enabled Standing Gumball Model #2004"
        result += "\nInventory: %d gumball" % self.count
        if (self.count != 1):
            result += "s"

        result += "\n"
        result += "Machine is %s\n" % self.state
        return result
