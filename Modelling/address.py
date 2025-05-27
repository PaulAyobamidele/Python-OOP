class Person:
    def __init__(self, name, address, phoneNumber, birthday):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.birthday = birthday

    def showInfo(self):
        print()
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Birthday: {self.birthday}")


if __name__ == "__main__":
    person1 = Person("John Doe", "123 Main St, Springfield", "555-1234", "1990-01-01")
    person2 = Person("Jane Smith", "456 Elm St, Springfield", "555-5678", "1992-02-02")

    person1.showInfo()
    person2.showInfo()

    print(vars((person1)))
    print(vars((person2)))
