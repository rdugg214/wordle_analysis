import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_hints_table(answers: pd.Series):
    hints_table = pd.DataFrame(
        {
            "answers": answers,
            "first_letter": answers.str[0],
            "length": answers.str.len(),
        }
    )
    hints_table = (
        hints_table.groupby(["first_letter", "length"])["answers"].count().unstack()
    )
    hints_table.fillna(0, inplace=True)
    hints_table = hints_table.astype(int)
    return hints_table


def prep_words():
    # loading of dataset
    all_words = pd.read_csv(
        "datasets/words_spelling_bee.txt", delimiter=" ", header=None
    )[0]

    # prepping of dataset
    all_words.drop(all_words[all_words.isna()].index, inplace=True)
    all_words.drop(all_words[all_words.str.len() < 4].index, inplace=True)

    return all_words


def get_answers(all_words: pd.Series, central_letter: str, spelling_bee_letters: set):
    # check contains central letter
    central_mask = all_words.str.contains(central_letter)

    # check contains only letters from set
    unique_characters = all_words.apply(set)
    valid_answer_mask = unique_characters.apply(
        lambda x: x.issubset(spelling_bee_letters)
    )

    valid_answer_mask = central_mask & valid_answer_mask

    spelling_bee_answers = all_words[valid_answer_mask]

    return spelling_bee_answers


def get_pangrams(answers: pd.Series):
    # pangrams
    answers_letter_set = answers.apply(set)
    pangram_mask = answers_letter_set.apply(lambda x: len(x)) == 7
    pangrams = answers[pangram_mask]

    # perfect pangrams
    perfect_pangram_mask = pangrams.str.len() == 7
    perfect_pangrams = pangrams[perfect_pangram_mask]

    return pangrams


def solve_get_hints(
    all_words: pd.Series, central_letter: str, spelling_bee_letters: set
):
    answers = get_answers(all_words, central_letter, spelling_bee_letters)
    pangrams = get_pangrams(answers)
    hints_table = create_hints_table(answers)
    pangram_hints_table = create_hints_table(pangrams)
    return answers, pangrams, hints_table, pangram_hints_table


def main():
    central_letter = "h"
    set_letters = ["l", "n", "t", "e", "i", "o"]
    spelling_bee_letters = set(set_letters + [central_letter])

    all_words = prep_words()

    answers, pangrams, hints_table, pangram_hints_table = solve_get_hints(
        all_words, central_letter, spelling_bee_letters
    )

    print(hints_table)
    print(pangram_hints_table)


if __name__ == "__main__":
    main()
