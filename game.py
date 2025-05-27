class Player:
    def __init__(self, name, points, health, location):
        self.name = name
        self.points = points
        self.health = health
        self.location = location

    def Addpoints(self, points):
        self.points += points

    def Removepoints(self, points):
        if self.points >= points:
            self.points -= points
        else:
            print("Not enough points to remove.")

    def showInfo(self):
        print()
        print(
            f"Player Name: {self.name}, Points: {self.points}, Health: {self.health}, Location: {self.location}"
        )


if __name__ == "__main__":
    player1 = Player("Ben", 79, 80, "Ibadan")
    player2 = Player("Jude", 92, 72, "Ibadan")
    player3 = Player("Paul", 100, 100, "Quebec")

    player1.showInfo()
    player2.showInfo()
    player3.showInfo()

    player1.Addpoints(20)
    player1.showInfo()

    player2.Removepoints(10)
    player2.showInfo()
    player1.Removepoints(100)  # Attempt to remove more points than available
    player1.showInfo()
