import pandas as pd
import numpy as np

class Wordle():
    def __init__(self):
        self.target_word:str = None
        self.words:pd.Series = None

    def create_new_game(self, target_word:str=None, seed=None):
        self.__ensure_word_list()
        self.guess_count = 0

        if target_word is None:
            target_word = self.__select_random_word(seed=seed)

        self.target_word = target_word

    def make_guess(self, guess_word) -> list:
        if self.guess_count > 6:
            print(f"Sorry you already ran out of guesses, the word was '{self.target_word}', try again")
            return None

        self.guess_count += 1

        if self.__is_invalid(guess_word):
            return None

        guess_accuracy = self._compare_words(guess_word)

        self.__check_winner(guess_accuracy)

        return guess_accuracy
    
    def _compare_words(self, guess_word:str) -> list:
        guess_accuracy = [0, 0, 0, 0, 0]
        guess_accuracy = self.__is_correct(guess_word, guess_accuracy)
        guess_accuracy = self.__is_patially_correct(guess_word, guess_accuracy)

        return guess_accuracy

    def __ensure_word_list(self):
        if not self.words is None:
            return

        self.words = pd.read_csv("./datasets/words.txt", header=None).iloc[:, 0]

    def __select_random_word(self, seed:int=None):
        if not seed is None:
            np.random.seed = seed
        return self.words[np.random.randint(0, len(self.words))]

    def __is_invalid(self, guess_word:str):
        return guess_word == self.words.any()

    def __is_correct(self, guess_word, guess_accuracy) -> list:
        for i in range(len(guess_word)):
            if guess_word[i] == self.target_word[i]:
                guess_accuracy[i] = 2

        return guess_accuracy

    def __is_patially_correct(self, guess_word, guess_accuracy) -> list:
        for i in range(len(guess_word)):
            if guess_accuracy[i] == 2:
                continue

            current_letter = guess_word[i]
            in_word = current_letter in self.target_word
            if not in_word:
                continue

            target_dup_count = 0
            for j in range(len(self.target_word)):
                if self.target_word[j] == current_letter:
                    target_dup_count += 1

            accounted_for_guesses = 0
            for j in range(len(guess_word)):
                if guess_word[j] != current_letter:
                    continue
                
                if j < i or guess_accuracy[j] == 2:
                    accounted_for_guesses += 1


            if accounted_for_guesses < target_dup_count:
                guess_accuracy[i] = 1

        return guess_accuracy

    def __check_winner(self, guess_accuracy):
        # Check if the guess was correct
        total_score = 0
        for score in guess_accuracy:
            total_score += score

        if score == 10:
            print(f"Congratuations you did it, you solved for the word '{self.target_word}' in just {self.guess_count} guesses!")
        elif self.guess_count > 6:
            print(f"Better luck next time. The correct answer was '{self.target_word}'")


class WordleInfinite(Wordle):
    def make_guess(self, guess_word) -> list:
        return super()._compare_words(guess_word)
