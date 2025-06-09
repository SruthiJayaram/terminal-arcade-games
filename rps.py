import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0
    def play_rps():
        class RPS(Enum):
            nonlocal game_count
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter ...\n1 for Rock,\n2 for Paper or\n3 for Scissors:\n\n")
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computerchoice == 3:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == 2 and computerchoice == 1:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == 3 and computerchoice == 2:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😔"
        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: { game_count}")
        print(f"\n{name}'s Wins: { player_wins}")
        print(f"\nPython Wins: { python_wins}")
        print(f"\n Play Again, {name}?")
        while True:
            playagain = input(" \n Y for Yes or \n Q to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return play_rps()
        else:
            print("\n🥳🥳🥳🥳🥳🥳")
            print("Thank You for playing\n\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    return play_rps



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
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()