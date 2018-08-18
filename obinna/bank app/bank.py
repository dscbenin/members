# Bank app implementation
# using OOP approach

# Base Class

class Account:

    #initialisation phase
    def __init__(self, name, amount):
        self.name = str(name)
        self.balance = float(amount) if self.valid(amount) else 0.0 ## set to stable state

    # sanitizing functions
    def valid(self, value):
        if value < 0:
            return False
        return True

    def sufficient(self, value):
        if value > self.balance:
            return False
        return True

    # function for deposits
    def deposit(self, amount):
        if not self.valid(amount):
            print("amount is not valid!!")
            return
        self.balance += amount
        print("Deposit of {amount} to {name} was successfull \nAvailable balance is ${balance}".format(amount=amount, name=self.name, balance=self.balance))


    def withdraw(self, amount):
        if not self.valid(amount):
            print("amount is not valid!!")
            return
        elif not self.sufficient(amount):
            print("Insufficient balance...")
            return
        self.balance -= amount
        print("Withdrawal was successfull \n Remaining balance is ${balance}".format(balance=self.balance))



# Creating an account instance

account1 = Account("Obinna", 700)

#print account1 balance
print(account1.balance)

#deposit 100 to account1
account1.deposit(100)

# updated balance
print(account1.balance)

# withdraw 300
account1.withdraw(300)

# update balance
print(account1.balance)





