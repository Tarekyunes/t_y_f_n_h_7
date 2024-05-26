# Question 4: Object-Oriented Programming - Bank Class
# Define a class BankAccount with the following attributes and methods:
# Attributes: account_number (string), account_holder (string), balance (float, initialized to 0.0)
# Methods:deposit(amount), withdraw(amount) , get_balance()
# - Create an instance of BankAccount, - Perform a deposit of $1000, - Perform a withdrawal of $500.
# - Print the current balance after each operation.
# - Define a subclass SavingsAccount that inherits from BankAccount and adds interest_rate Attribute and
# apply_interest() method that Applies interest to the balance based on the interest rate.
# And Override print() method to print the current balance and rate.
# - Create an instance of SavingsAccount , and call apply_interest() and print() functions.

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"the current balance: {self.balance}"
        else:
            return "invalid deposit amount"

    def withdraw(self, amount):
        if (amount > 0) and (amount <= self.balance):
            self.balance -= amount
            return f"the current balance after withdraw: {self.balance}"
        else:
            return "invalid withdrawal amount or insufficient funds"


account = BankAccount("7777337", "Tarek")
print(account.deposit(1000))
print(account.withdraw(500))


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance = self.balance + (self.interest_rate/100)*self.balance

    def __str__(self):
        return f"the current balance: {self.balance} and the interest rate : {self.interest_rate}"


saving_account = SavingsAccount("77777", "younes", 7)
saving_account.deposit(1000)
saving_account.apply_interest()
print(saving_account)