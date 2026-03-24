from spelling_bee import prep_words, solve_get_hints

def get_game_details():
    central_letter = input("Input central letter: ")
    set_letters = []
    for i in range(6):
        set_letters.append(input(f"Input outer letter {i+1}: "))

    spelling_bee_letters = set(set_letters + [central_letter])
    return central_letter, spelling_bee_letters

def main():
    all_words = prep_words()
    print("Input spelling bee letters")
    central_letter, spelling_bee_letters = get_game_details()

    answers, pangrams, hints_table, pangram_hints_table = solve_get_hints(all_words, central_letter, spelling_bee_letters)

    print("Hints table")
    print(hints_table)

    input("Would you like to see pangram hints?")
    print(pangram_hints_table)

    input("Would you like initial letters?")
    print(pangrams.str[:2].values)

    for i in range(3, 7):
        input("Another letter?")
        print(pangrams.str[:i].values)

    input("Full reveal?")
    print(pangrams.values)

    input("All words?")
    print(answers)

if __name__ == "__main__":
    main()