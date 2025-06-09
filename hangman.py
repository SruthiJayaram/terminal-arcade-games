import sys
import random

def hm(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    
    def play_hangman():
        nonlocal game_count
        nonlocal name
        nonlocal player_wins
        with open("words.txt", "r") as f:
            words = [
                line.strip().lower()
                for line in f
                if all(c.isalpha() or c.isspace() for c in line.strip())
            ]
        if not words:
            print("No valid words found in words.txt.")
            return
        
        word = random.choice(words)
        guessed_letters = set()
        attempts_left = 7
        
        while True:
            display_word = " ".join([char if char in guessed_letters or char == " " else "_" for char in word])
            
            print(f"\nWord: {display_word}")
            if guessed_letters:
                print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
                print(f"Attempts left: {attempts_left}")

            if "_" not in display_word:
                print("\nYou guessed it!")
                player_wins += 1
                print(f"The word was: {word}")
                break

            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Enter a single alphabetic character.")
                continue

            if guess in guessed_letters:
                print("Already guessed.")
                continue

            guessed_letters.add(guess)

            if guess not in word:
                attempts_left -= 1
                print("Incorrect!")

            if attempts_left == 0:
                print(f"\nGame over! The word was: {word}")
                break
            
        game_count += 1
        print(f"\nGame Count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
            
        while True:
            playagain = input(" \n Y for Yes or \n Q to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return play_hangman()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank You for playing\n\n")
            if __name__ == "__main__":     #so that this hangman runs on its own
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return play_hangman

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides personalized game expeience."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
    args = parser.parse_args()
    hangman = hm(args.name)
    hangman()
        