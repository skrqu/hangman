import random

def get_random_word():
    words = [
        'python', 'hangman', 'challenge', 'programming', 'computer',
        'random', 'function', 'variable', 'syntax', 'algorithm',
        'keyboard', 'monitor', 'internet', 'software', 'hardware'
    ]
    return random.choice(words)

def draw_hangman(wrong_guesses):
    stages = [
        """
         +---+
             |
             |
             |
            ===
        """,
        """ 
         +---+
         O   |
             |
             |
            ===
        """,
        """
         +---+
         O   |
         |   |
             |
            ===
        """,
        """
         +---+
         O   |
        /|   |
             |
            ===
        """,
        """
         +---+
         O   |
        /|\  |
             |
            ===
        """,
        """
         +---+
         O   |
        /|\  |
        /    |
            ===
        """,
        """
         +---+
         O   |
        /|\  |
        / \  |
            ===
        """,
        """
         +---+
        [O   |
        /|\  |
        / \  |
            ===
        """,
        """
         +---+
        [O]  |
        /|\  |
        / \  |
            ===
        """,
        """
         +---+
        [O]  |
        /|\  |
        / \  |
       GAME OVER
            ===
        """
    ]
    print(stages[min(wrong_guesses, len(stages)-1)])

def play_hangman():
    while True:
        word = get_random_word()
        guessed = set()
        wrong_guesses = 0
        max_wrong = 10
        print("\nWelcome to Hangman!")
        while wrong_guesses < max_wrong:
            display_word = ' '.join([letter if letter in guessed else '_' for letter in word])
            print(f"\nWord: {display_word}")
            draw_hangman(wrong_guesses)
            guess = input("Guess a letter or the whole word: ").lower()
            if not guess.isalpha():
                print("Please enter only letters.")
                continue
            if len(guess) == len(word) and guess == word:
                print(f"\nCongratulations! You guessed the word: {word}")
                break
            if len(guess) == 1:
                if guess in guessed:
                    print("You already guessed that letter.")
                    continue
                guessed.add(guess)
                if guess not in word:
                    wrong_guesses += 1
                    print(f"Wrong! You have {max_wrong - wrong_guesses} guesses left.")
                else:
                    print("Good guess!")
            else:
                print("Incorrect word guess.")
                wrong_guesses += 1
                print(f"Wrong! You have {max_wrong - wrong_guesses} guesses left.")
            if all(letter in guessed for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            draw_hangman(wrong_guesses)
            print(f"\nSorry, you lost! The word was: {word}")
        play_again = input("\nPlay another round? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    play_hangman()
