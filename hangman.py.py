import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "code", "developer", "game",  "elephant", "chocolate", "basketball", "pineapple", "universe",
    "adventure", "strawberry", "technology", "happiness", "butterfly","astronaut", "waterfall", "spaghetti", "firefly", "friendship",
    "sunshine", "magician", "treasure", "cathedral", "galaxy"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def main():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts -= 1

        if '_' not in display_word(word, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break

        print("Attempts left:", attempts)

    if attempts == 0:
        print("\nSorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    main()
