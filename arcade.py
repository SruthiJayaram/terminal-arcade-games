import sys
from rps import rps
from guessnumber import gn
from hangman import hm
from tictactoe import ttt


def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu🎯.")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n3 = Hangman\n4 = Tic-Tac-Toe\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "3", "4", "x"]:
            print(f"\n{name}, please enter 1, 2, 3, 4 or x.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = gn(name)
            guess_my_number()
        elif playerchoice == "3":
            hangman = hm(name)
            hangman()
        elif playerchoice == "4":
            tictactoe = ttt(name)
            tictactoe()
        else:
            print(f"\n{name}, thanks for playing! 🎮")
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    play_game(args.name)