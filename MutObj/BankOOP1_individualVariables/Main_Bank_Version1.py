from account import *

JohnAccount = Account("John", 100, "JohnPassword")
print("Created an account for John")


MarysAccount = Account("Mary", 300, "MaryPassword")
print("Created an account for Mary")


JohnAccount.show()
MarysAccount.show()
print("*" * 20)


print("Calling methods of the two accounts...")
JohnAccount.deposit(50, "JohnPassword")
MarysAccount.withdraw(100, "MaryPassword")
MarysAccount.deposit(100, "MaryPassword")


JohnAccount.show()
MarysAccount.show()


print("-" * 20)
userName = input("what is the name for the new user account?")
userBalance = input("what is the starting balance for this account?")
userBalance = int(userBalance)
userPassword = input("what is the password you want to use for this account?")
NewAccount = Account(userName, userBalance, userPassword)


NewAccount.show()


NewAccount.deposit(100, userPassword)
userBalance = NewAccount.getBalance(userPassword)
print()
print("After depositing 100, the new balance is:", userBalance)


NewAccount.show()
