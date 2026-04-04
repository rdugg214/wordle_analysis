from nyt_games.games.wordle.wordle_game import Wordle, WordleInfinite


def test_setup():
    wordle = Wordle()
    wordle.create_new_game("quick")


def test_guess_invalid():
    wordle = Wordle()
    wordle.create_new_game("quick")

    # too long word
    assert wordle.make_guess("toolongword") is None
    # invalid characters
    assert wordle.make_guess("92013") is None
    assert wordle.make_guess("CAPSS") is None


def test_guess_all_incorrect():
    wordle = Wordle()
    wordle.create_new_game("quick")

    assert [0, 0, 0, 0, 0] == wordle.make_guess("babes")


def test_guess_duplicated_letters():
    wordle = Wordle()
    wordle.create_new_game("abbey")
    assert [1, 1, 2, 2, 0] == wordle.make_guess("babes")
    assert [0, 1, 2, 1, 1] == wordle.make_guess("kebab")
    assert [0, 1, 0, 0, 0] == wordle.make_guess("keeps")

    wordle.create_new_game("about")
    assert [0, 2, 0, 0, 0] == wordle._compare_words("bbbbb")


def test_full_games():
    wordle = Wordle()
    wordle.create_new_game("abbey")
    wordle.make_guess("kebab")
    wordle.make_guess("kebab")
    wordle.make_guess("kebab")
    wordle.make_guess("kebab")
    wordle.make_guess("kebab")
    wordle.make_guess("kebab")

    assert wordle.make_guess("kebab") is None

    wordle = Wordle()
    wordle.create_new_game("abbey")
    wordle.make_guess("kebab")
    wordle.make_guess("invalid word")
    wordle.make_guess("kebab")
    wordle.make_guess("invalid word")
    wordle.make_guess("kebab")
    wordle.make_guess("invalid word")
    wordle.make_guess("kebab")
    wordle.make_guess("invalid word")
    wordle.make_guess("kebab")
    wordle.make_guess("invalid word")
    wordle.make_guess("kebab")
    wordle.make_guess("invalid word")

    assert wordle.make_guess("kebab") is None
