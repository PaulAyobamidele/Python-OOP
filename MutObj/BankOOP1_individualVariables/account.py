class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToDeposit < 0:
            print("Sorry, you cannot deposit a negative amount")
            return None

        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToWithdraw < 0:
            print("Sorry, you cannot withdraw a negative amount")
            return None
        if amountToWithdraw > self.balance:
            print("Sorry, you cannot withdraw more than your balance")
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None

        return self.balance

    def show(self):
        print(f"Account Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Password: {'*' * len(self.password)}")


oAccount = Account("John Doe", 1000, "Morocco")
newBalance = oAccount.deposit(500, "Morocco")
if newBalance is not None:
    print(f"New Balance after deposit: {newBalance}")
