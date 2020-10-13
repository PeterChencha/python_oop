from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    """docstring for Account"""

    @abstractmethod
    def createAccount(self, name, initialDeposit):
        pass

    @abstractmethod
    def authenticate(self, name, accountNumber):
        pass

    @abstractmethod
    def withdraw(self, withdrawAmount):
        pass

    @abstractmethod
    def deposit(self, depAmount):
        pass

    @abstractmethod
    def displayBalance(self):
        pass


class SavingsAccount(Account):
    """docstring for SavingsAccount."""

    def __init__(self):
        super(SavingsAccount, self).__init__()
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = self.random_with_N_digits(5)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication successful")
                return True
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficent funds")
        else:
            newAmount = self.savingsAccounts[self.accountNumber][1]
            - withdrawAmount
            self.savingsAccounts[self.accountNumber][1] = newAmount
            print("Withdraw was successful, new balance is ",
                  self.savingsAccounts[self.accountNumber][1])

    def deposit(self, depAmount):
        newAmount = self.savingsAccounts[self.accountNumber][1]
        + depAmount
        self.savingsAccounts[self.accountNumber][1] = newAmount
        print("Withdraw was successful, new balance is ",
              self.savingsAccounts[self.accountNumber][1])

    def displayBalance(self):
        return self.savingsAccounts[self.accountNumber][1]

    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
