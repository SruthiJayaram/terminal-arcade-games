import sys
import random

def ttt(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0
    def play_ttt():
        nonlocal game_count
        nonlocal player_wins
        nonlocal name
        board = [' ' for _ in range(9)]
        current_player = 'X'
        def print_board():
            print("\n")
            print(f" {board[0]} | {board[1]} | {board[2]} ")
            print("---|---|---")
            print(f" {board[3]} | {board[4]} | {board[5]} ")
            print("---|---|---")
            print(f" {board[6]} | {board[7]} | {board[8]} ")
            print("\n")
            
        def check_winner():
            win_combos = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]        
            ]
            return any(
                all(board[i] == current_player for i in combo) for combo in win_combos
            )
            
        def is_full():
            return all(cell != ' ' for cell in board)
        while True:
            print_board()
            try:
                move = int(input(f"{name} ({current_player}), enter your move (0-8): "))
                if move < 0 or move >= 9 or board[move] != ' ':
                    print("\nInvalid move. Try again.")
                    continue
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 9.")
                continue
            
            board[move] = current_player
            
            if check_winner():
                print_board()
                print(f"\n🎉🎉{name} wins as ({current_player})!")
                player_wins += 1
                break
            
            if is_full():
                print_board()
                print("\nIt's a tie 🫨!")
                break
            
            current_player = "O" if current_player == "X" else "X"
            game_count += 1
            print(f"\n Count: {game_count}")
            print(f"\n{name} Wins: {player_wins}")
            print(f"\n\nPlay again, {name}?") 
        while True:
            play_again = input("\nY for Yes,\nQ for Quit\n ")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if play_again.lower() == 'y':
                return play_ttt()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank You for playing\n\n")
            if __name__ == "__main__":     #so that this tictactoe runs on its own
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    return play_ttt

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
    tictactoe = ttt(args.name)
    tictactoe()

        