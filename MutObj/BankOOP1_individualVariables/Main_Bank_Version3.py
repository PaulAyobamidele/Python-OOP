from account import *

accountsDict = {}
nextAccountNumber = 0


oAccount = Account("John", 100, "JohnPassword")
johnAccountNumber = nextAccountNumber
accountsDict[johnAccountNumber] = oAccount
print("Account number for Joe is: ", johnAccountNumber)
nextAccountNumber = nextAccountNumber + 1


oAccount = Account("Mary", "200", "MarysPassword")
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print("Account number for Mary is:", marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[johnAccountNumber].show()
accountsDict[marysAccountNumber].show()
print("-" * 10)


print("Calling methods on the two accounts")
accountsDict[johnAccountNumber].deposit(50, "JohnPassword")
accountsDict[marysAccountNumber].withdraw(10, "MarysPassword")
accountsDict[marysAccountNumber].deposit(100, "MarysPassword")


accountsDict[johnAccountNumber].show()
accountsDict[marysAccountNumber].show()


print("-" * 10)
userName = input("please provide you full name to open a new user account? ")
userBalance = input("What is the starting balance for this account?")
userBalance = int(userBalance)
userPassword = input("What is your password for this account?")
oAccount = Account(userName, userBalance, userPassword)

newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = (
    oAccount  # This is an expression to instantiate a new key-value pair in dictionaries
)

print("Account number for new account is: ", newAccountNumber)
nextAccountNumber = nextAccountNumber + 1


accountsDict[newAccountNumber].show()


accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print("*" * 20)
print("After depositing 100, the user's balance is: ", userBalance)

accountsDict[newAccountNumber].show()
