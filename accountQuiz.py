# The Account class simulates a bank account.
# Quiz on Classes and Inheritances Part One:

class Account:

    __interestRate = .045
    
    # Defining priviate variables
    
    def __init__(self, bal):
        self.__balance = bal

    def id(self, number):
        self.__id = number

    def interest(self, intrate):
        self.__interest = intrate
    

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount
    # from the account.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    
    # The monthlyinterestrate method returns interest
    def get_interest(self, amount):
        return self.__balance + amount * intrate
    

    # The get_balance method returns the
    # account balance.

    def get_balance(self):
        return self.__balance

    def get_interest(self):
        return self.__interest
