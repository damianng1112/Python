
from tkinter import messagebox


class Counter:

    def __init__(self, val):
        self.__value = val
        self._message=''

    def getValue(self):
        return self.__value

    def increment(self):
        self.__value += 1
    
    def decrement(self):
        self.__value -= 1

    def writeMessage(self, msg):
        self._message=msg

    def readMessage(self):
        return self._message


#------------end of class definition------------------
# Decorator

class Decorator(Counter):

    def __init__(self, cc):
        super.__init__(0)
        self._counter = cc


    #Trace Amount
class UpperLimit(Decorator):

    def __init__(self, cc):
        super.__init__(cc)

    def getValue(self):
        return self._counter.getValue()

    def increment(self):
        if self._counter.getValue() == 20:
            self.writeMessage("UpperLimit Reached")
        else:
            self._counter.increment()

    def decrement(self):
        self._counter.decrement()

    def writeMessage(self, msg):
        self._counter.writeMessage(msg)

    def readMessage(self):
        return self._counter.readMessage()

    #NoOverdraft  Account


class LowerLimit(Decorator):

    def __init__(self, cc):
        super.__init__(cc)

    def getValue(self):
        return self._counter.getValue()

    def increment(self):
        self._counter.increment()

    def decrement(self):
        if self._counter.getValue() == 0:
            self.writeMessage("Already 0")
        else:
            self._counter.decrement()

    def writeMessage(self, msg):
        self._counter.writeMessage(msg)

    def readMessage(self):
        return self._counter.readMessage()
