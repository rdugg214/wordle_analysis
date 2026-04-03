from wordle_game import Wordle, WordleInfinite

def test_setup():
    pass

def test_guess_invalid():
    pass

def test_guess_all_incorrect():
    wordle = Wordle()
    wordle.create_new_game("quick")
    
    pass

def test_guess_duplicated_letters():
    wordle = Wordle()
    
    wordle.create_new_game("abbey")
    assert [1, 1, 2, 2, 0] == wordle.make_guess("babes")
    assert [0, 1, 2, 1, 1] == wordle.make_guess("kebab")
    assert [0, 1, 0, 0, 0] == wordle.make_guess("keeps")

    WordleInfinite()
    wordle.create_new_game("about")
    assert [0, 2, 0, 0, 0] == wordle.make_guess("bbbbb")


if __name__ == "__main__":
    test_setup()
    test_guess_invalid()
    test_guess_all_incorrect()
    test_guess_duplicated_letters()

