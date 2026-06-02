import random


WORDS = ["python", "coding", "intern", "github", "project"]
MAX_WRONG_GUESSES = 6


def show_word(secret_word, guessed_letters):
    display = []

    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")

    return " ".join(display)


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", show_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print("Wrong guesses left:", MAX_WRONG_GUESSES - wrong_guesses)

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("Word:", show_word(secret_word, guessed_letters))
            print("Congratulations! You guessed the word!")
            break
    else:
        print("Game over!")
        print("The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
