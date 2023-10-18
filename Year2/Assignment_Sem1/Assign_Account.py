class Account:

    def __init__(self, name, accountNo, balance, bankrupt, status):
        self.__name = name
        self.__accountNo = accountNo
        self.__balance = balance
        self.__amount = 0
        self.__bankrupt = bankrupt
        self.__status = status

    def deposit(self, amount):
        self.__balance += amount
        if self.__balance >= 0:
            self.__bankrupt = False

    def withdraw(self, amount):
        self.__balance -= amount
        if self.__balance <= 0:
            self.__bankrupt = True
        else:
            self.__bankrupt = False

    def getBalance(self):
        return self.__balance

    def getBankrupt(self):
        return  self.__bankrupt

    def getAmount(self):
        return self.__amount

    def getName(self):
        return self.__name

    def getAccountNo(self):
        return self.__accountNo

    def getStatus(self):
        return self.__status

    def getIntRate(self):
        if self.__status == 'Non-member':
            rate = 3
        elif self.__status == 'Member':
            rate = 2
        else:
            rate = 1
        return rate

    def calcTax(self, rate):
        res = float(float(self.__balance) * (rate/100))
        return round(res, 2)
