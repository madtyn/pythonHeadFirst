'''
Created on 26/2/2016

@author: madtyn
'''

# NOTE: This is not thread safe!

class Singleton:
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Empty Constructor
        '''
        # other useful instance variables here
        self.uniqueInstance = None

    def getInstance(self):
        if self.uniqueInstance == None:
            self.uniqueInstance = Singleton()
        return self.uniqueInstance

    # other useful methods here
