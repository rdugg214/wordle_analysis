from abc import abstractmethod

from wordleanalysis.wordle_game import Wordle
from wordleanalysis.solvers.GameDetails import GameDetails

class WordleSolver:
    def __init__(self) -> None:
        pass

    def attempt_solve(self, wordle_game: Wordle) -> GameDetails:
        number_guesses = 5
        game_details = GameDetails()
        for i in range(number_guesses):
            guess_word = self.guess()
            guess_score = wordle_game.make_guess(guess_word)

            game_details.add_guess(guess_word, guess_score)
            
            if self._is_solved(guess_score):
                break

            self.prepare_next_guess(guess_word, guess_score)

        if not self._is_solved(guess_score):
            game_details.ran_out_of_guesses()

        return game_details
    
    @abstractmethod
    def guess(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def prepare_next_guess(self, guess_word: str, guess_score: list[int]):
        raise NotImplementedError
    
    def _is_solved(self, guess_score:list[int]) -> bool:
        total_score = 0
        for score in guess_score:
            total_score += score

        return total_score == 10

