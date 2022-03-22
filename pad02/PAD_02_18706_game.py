from enum import Enum
from random import random


class Difficulty(Enum):
    Beginner = 8
    Intermediate = 5
    Advanced = 3


class Game():

    def __init__(self, players):
        self.players = players

    def _play(self):
        print("Game started...")


class Hangman(Game):

    def __init__(self, players, difficulty):
        super().__init__(players)
        self.difficulty = difficulty
        self.max_bad_tries = difficulty.value
        self.letter_list = set()

    def start_game(self):
        super()._play()
        if self.players == 1:
            word = self.generate_word()
        else:
            word = input()
        word = "urstary"

        is_solved = False
        bad_tries = 0
        while bad_tries < self.max_bad_tries and not is_solved:
            print("Write letter: ")
            # print(f"Word is {word}")
            self.letter_list.add(self.get_letter())
            bad_tries += 1
            print(f"{bad_tries} and {self.letter_list}")

    def get_letter(self):
        return input()

    def generate_word(self):
        random()


game_1 = Hangman(1, Difficulty.Intermediate)
game_1.start_game()
