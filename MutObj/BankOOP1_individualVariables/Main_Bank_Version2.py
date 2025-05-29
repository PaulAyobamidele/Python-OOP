from account import *


accountsList = []
JAccount = Account("John", 100, "JohnPassword")
accountsList.append(JAccount)
print("Joe's account number is 0")


MAccount = Account("Mary", 300, "MaryPassword")
accountsList.append(MAccount)
print("Mary's account number is 1")


accountsList[0].show()
accountsList[1].show()
print("*" * 20)

print("Calling methods of the two accounts...")
accountsList[0].deposit(50, "JohnPassword")
accountsList[1].withdraw(100, "MaryPassword")
accountsList[1].deposit(100, "MaryPassword")


accountsList[0].show()
accountsList[1].show()

print("-" * 20)
userName = input("What is the name for the new user account? ")
userBalance = input("What is the starting balance for this account? ")
userBalance = int(userBalance)
userPassword = input("What is the password you want to use for this account? ")
Account = Account(userName, userBalance, userPassword)
accountsList.append(Account)

print("Created a new account for", userName)
print("The new account number is", len(accountsList) - 1)
accountsList[-1].show()


accountsList[-1].deposit(100, userPassword)
userBalance = accountsList[-1].getBalance(userPassword)
print()
print("After depositing 100, the new balance is:", userBalance)
accountsList[-1].show()
print("All accounts in the system:")
for i, account in enumerate(accountsList):
    print(f"Account {i}:")
    account.show()
    print("-" * 20)
print("Thank you for using the bank system!")
