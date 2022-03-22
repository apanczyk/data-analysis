# TASK 4

class Game():
    def __init__(self, players=5):
        self.players = players

    def _play(self):
        print("Game started...")


class Hangman(Game):
    def __init__(self):
        super().__init__(4)

    def asd(self):
        return "Asd"


Gra1 = Hangman()
