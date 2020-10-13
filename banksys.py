from random import randint


class Account(object):
    """docstring for Account."""

    def __init__(self, accName, initialDeposit):
        super(Account, self).__init__()
        self.accName = accName
        self.initialDeposit = initialDeposit
        self.accountNumber = None
        self.accountAmount = initialDeposit

    def generateAccNumber(self):
        accNumber = self.random_with_N_digits(5)
        self.accountNumber = accNumber

    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)


class User(Account):
    """docstring for User."""

    def verifiyAccount(self, name, accNo):
        if name == self.accName and accNo == self.accountNumber:
            print("Welcome back ", self.accName)
        else:
            print("You Dont have an account")

    def withdraw(self, withdrawAmount):
        self.accountAmount = self.accountAmount = withdrawAmount
        print("Withdraw Was Successful")

    def deposit(self, depAmount):
        self.accountAmount = self.accountAmount + depAmount
        print("Deposit Was Successful")

    def displayAmmount(self):
        return self.accountAmount


account = Account("Peter", 10000)
account.generateAccNumber()
print(account.accountNumber)
user = User()
