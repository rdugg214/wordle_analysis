import pandas as pd

class GameDetails:
    def __init__(self) -> None:
        self.guesses = []
        self.guess_scores = []
        self.number_guesses = 0

    def add_guess(self, guess_word:str, guess_score:list[int]):
        self.guesses.append(guess_word)
        self.guess_scores.append(guess_score)
        self.number_guesses += 1

    def ran_out_of_guesses(self):
        self.number_guesses = -1

    def get_details_dict(self) -> dict:
        return {
            "guesses": self.guesses,
            "guess_scores": self.guess_scores,
            "final_number_guesses": self.number_guesses,
        }