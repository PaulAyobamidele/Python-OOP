class Student:
    def __init__(self, name, emailAddress, currentGrade):
        self.name = name
        self.emailAddress = emailAddress
        self.currentGrade = currentGrade

    def __str__(self):
        return (
            f"Name: {self.name}, Email: {self.emailAddress}, Grade: {self.currentGrade}"
        )

    def __repr__(self):
        return f"Student(name={self.name}, emailAddress={self.emailAddress}, currentGrade={self.currentGrade})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (
                self.name == other.name
                and self.emailAddress == other.emailAddress
                and self.currentGrade == other.currentGrade
            )
        return False

    def __hash__(self):
        return hash((self.name, self.emailAddress, self.currentGrade))

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.currentGrade < other.currentGrade
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.currentGrade <= other.currentGrade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.currentGrade > other.currentGrade
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.currentGrade >= other.currentGrade
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return not self.__eq__(other)
        return NotImplemented

    def details(self):
        print()
        print(
            f"Name: {self.name}, Email: {self.emailAddress}, Grade: {self.currentGrade}"
        )


if __name__ == "__main__":

    Shade = Student("Shade", "shade.um6p.ma", 17)
    Tola = Student("Tola", "tola.um6p.ma", 18)

    Shade.details()
    Tola.details()
