import sys
import random

def gn(name = "PlayerOne"):
    game_count = 0
    player_wins = 0
    def play_gn():
        nonlocal game_count
        nonlocal name
        nonlocal player_wins
        playerchoice = input(
        f"\n{name}, guess which number I'm thinking of... between 1 and 100.\n\n"
        )
        
        if not playerchoice.isdigit():
            print(f"{name}, please enter a valid number.")
            return play_gn()
        
        player = int(playerchoice)
        
        if not  1 <= player <= 100:
            print(f"{name}, please enter a number between 1 and 100.")
            return play_gn()
            
        computerchoice = random.randint(1, 100)
        
        print(f"\n{name}, you chose {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        computer = int(computerchoice)
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 🥲"
        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: { game_count}")
        print(f"\n{name}'s wins: { player_wins}")
        print(f"\n Play Again, {name}?")   
        
    
        while True:
            playagain = input(" \n Y for Yes or \n Q to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return play_gn()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank You for playing\n\n")
            if __name__ == "__main__":     #so that this guess number runs on its own
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    return play_gn

#for arcade
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
    guess_number = gn(args.name)
    guess_number()