from Bank import *


oBank = Bank()


johnsAccountNumber = oBank.createAccount("John", 100, "JohnsPassword")
print("John's account number is: ", johnsAccountNumber)

marysAccountNumber = oBank.createAccount("Mary", 120, "MarysPassword")
print("Mary's account number is: ", marysAccountNumber)


while True:
    print()
    print("To get an account balance, press b")
    print("To close down your account, press c")
    print("To deposit some money, press d")
    print("To open an account press o")
    print("To exit the process, press q")
    print("To show the account details press s")
    print("To withdraw some money press w")

    action = input("Please enter a letter for your action")
    action = action.lower()
    action = action[0]

    print()

    if action == "b":
        oBank.balance()

    elif action == "c":
        oBank.closeAccount()

    elif action == "d":
        oBank.deposit()

    elif action == "o":
        oBank.openAccount()

    elif action == "q":
        break

    elif action == "s":
        oBank.show()

    elif action == "w":
        oBank.withdraw()

    else:
        print("Sorry, that was not a valid action, Try Again.")


print("Done")
