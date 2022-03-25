from enum import Enum
import random


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

    words_file = 'words.txt'

    def __init__(self, players, difficulty):
        super().__init__(players)
        self.difficulty = difficulty
        self.max_bad_tries = difficulty.value
        self.letter_list = set()

    def init_game():
        players = int(input(f"Please, choose 1 or 2 players (1,2)\n"))
        difficulty = int(
            input(
                f"Please, choose difficulty level (3 - advanced, 5 - intermediate, 8 - beginner)\n"
            ))
        try:
            if players not in (1, 2):
                raise Exception('Input should be only 1 or 2')
            if difficulty not in (3, 5, 8):
                raise Exception('Input should be in 3/5/8')
        except Exception as error:
            print(f'\n\n{repr(error)}\n\n')
            Hangman.init_game()
            return
        hangman = Hangman(players, Difficulty(difficulty))
        hangman.start_game()

    def start_game(self):
        super()._play()

        word = self.generate_word()
        bad_tries = 0
        anonymized = self.replace_letters(word, self.letter_list)

        while bad_tries < self.max_bad_tries and '_' in anonymized:
            self.print_welcome(word, bad_tries, anonymized)
            try:
                bad_tries = self.validate_letter(word, bad_tries)
            except Exception as error:
                print(f'\n\n{repr(error)}\n\n')
            anonymized = self.replace_letters(word, self.letter_list)

        result = 'guessed' if '_' not in anonymized else 'didnt guess'
        print(f'The word was {word} and you {result}')

    def print_welcome(self, word, bad_tries, anonymized):
        print(
            f'''\n=== Difficulty level {self.difficulty.name} ===\n\nBad tries: {bad_tries} and used letters: {self.letter_list}\nWrite letter:\n{anonymized}'''
            # f'''\n=== Difficulty level {self.difficulty.name} ===\n\nWord is {word}\nBad tries: {bad_tries} and used letters: {self.letter_list}\nWrite letter:\n{anonymized}'''
        )

    def validate_letter(self, word, bad_tries):
        used_letter = input()
        if len(used_letter) != 1 or not used_letter.isalpha():
            raise Exception('Input should be only one character')
        used_letter = used_letter.lower()

        if used_letter not in word and used_letter not in self.letter_list:
            bad_tries += 1
        self.letter_list.add(used_letter)

        return bad_tries

    def replace_letters(self, word, letter_list):
        word_to_return = list(word)
        for i in range(len(word)):
            word_to_return[i] = word[i] if (word[i] in letter_list) else '_'
        return word_to_return

    def generate_word(self):
        if self.players == 1:
            lines = open(self.words_file).read().splitlines()
            word = random.choice(lines)
        else:
            new_word = input("Please, write your own word: ")
            if len(new_word) < 2 or not new_word.isalpha():
                raise Exception('Wrong characters or too short')
            word = new_word.lower()
        return word


Hangman.init_game()
# game_1 = Hangman(1, Difficulty.Intermediate)
# game_1.start_game()
