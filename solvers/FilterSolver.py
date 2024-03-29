import pandas as pd

from WordleSolver import WordleSolver

class FilterSolver(WordleSolver):
    def __init__(self, guess_words:pd.Series, letter_masks:dict[pd.Series]) -> None:
        super().__init__()
        self.guess_words = guess_words
        self.words_matching_guess_mask = pd.Series(data=True, index=guess_words.index)
        self.letter_masks = letter_masks

    def guess(self) -> str:
        return self.guess_words[self.words_matching_guess_mask].iloc[0]["words"]
    
    def prepare_next_guess(self, guess_word: str, guess_score: list[int]):
        self.update_mask(guess_word, guess_score, letter_cols)
    
    def update_mask(self, guess_word:str, guess_score:list[int], letter_cols):
        for letter_score, letter, letter_col in zip(guess_score, guess_word, letter_cols):
            mask = self.letter_masks[letter][letter_col]

            if letter_score != 2:
                mask = ~mask

                non_zero_occurance_count = 0
                for letter_j, guess_score_j in zip(guess_word, guess_score):
                    if letter == letter_j and guess_score_j > 0:
                        non_zero_occurance_count += 1

                if letter_score == 1:
                    mask = mask & (self.letter_masks[letter]["occurance_sum"] >= non_zero_occurance_count)
                else:
                    mask = mask & (self.letter_masks[letter]["occurance_sum"] == non_zero_occurance_count)

            self.words_matching_guess_mask = self.words_matching_guess_mask & mask
            
    @staticmethod
    def calculate_letter_masks(guess_words, letter_cols) -> dict[pd.Series]:
        all_letters = [
            'e', 's', 'a', 'o', 'r', 'i', 'l', 't', 'n', 'u', 'd', 'p', 'm',
            'y', 'c', 'h', 'g', 'b', 'k', 'f', 'w', 'v', 'z', 'j', 'x', 'q'
        ]

        letter_masks = {}
        for letter in all_letters:
            letter_masks[letter] = {}
            letter_masks[letter]["occurance_sum"] = pd.Series(data=0, index=guess_words.index)
            for letter_col in letter_cols:
                mask = guess_words[letter_col] == letter
                letter_masks[letter][letter_col] = mask
                letter_masks[letter]["occurance_sum"] = letter_masks[letter]["occurance_sum"] + mask

        return letter_masks


