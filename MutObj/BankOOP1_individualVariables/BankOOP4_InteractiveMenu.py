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

while True:
    print()
    print("Press b to get the balance")
    print("Press d to deposit")
    print("Press o to open an account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0]

    print()
    if action == "b":
        print("*** Get Balance ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print("Your balance is: ", theBalance)

    elif action == "d":
        print("*** Deposit ***")
        userAccountNumber = input("Please enter the account number: ")
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input("Please enter the amount you intend to deposit")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter the password")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userAccountNumber, userPassword)
        if theBalance is not None:
            print("Your new balance is: ", theBalance)

    elif action == "o":
        print("*** Opening an Account ***")
        userName = input("Please enter your name for your new user account")
        userPassword = input("Please enter your preferred password")
        userStartingAmount = input("Please enter your starting deposit amount: ")
        userStartingAmount = int(userStartingAmount)
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print("Your new account number is:", nextAccountNumber)
        nextAccountNumber += 1
        print()

    elif action == "s":
        print("Show: ")
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print("     Account number:", userAccountNumber)
            oAccount.show()
    elif action == "q":
        break

    elif action == "w":
        print("*** Withdrawing ***")
        userAccountNumber = input("Please enter your account number correctly")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Please enter your password correctly")
        userWithdrawalAmount = input("How much would you like to withdraw?")
        userWithdrawalAmount = int(userWithdrawalAmount)
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)

        if theBalance is not None:
            print("Withdrew: ", userWithdrawalAmount)
            print("Your new balance is: ", theBalance)
    else:
        print("Sorry, that was not a valid action. Please try again.")


print("Done")
