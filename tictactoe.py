import sys
import random

def ttt(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    def play_ttt():
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal name
        
        while True:
            playersymbol = input(f"\n{name}, do you want to be 'X' or 'O'?\n").upper()
            if playersymbol in ['X', 'O']:
                break
            else:
                print("\nInvalid input. Please enter 'X' or 'O'.")
        if playersymbol == 'X':
            computer_symbol = 'O'
        else:
            computer_symbol = 'X'
        current_player = 'X'
        board = [' ' for _ in range(9)]
        def print_board():
            print("\n")
            print(f" {board[0]} | {board[1]} | {board[2]} ")
            print("---|---|---")
            print(f" {board[3]} | {board[4]} | {board[5]} ")
            print("---|---|---")
            print(f" {board[6]} | {board[7]} | {board[8]} ")
            print("\n")
            
        def check_winner_for(player):
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
        
        def min_max(is_maximizing):
            if check_winner_for(computer_symbol):
                return 1
            elif check_winner_for(playersymbol):
                return -1
            elif is_full():
                return 0
            
            if is_maximizing:
                best_score = -float('inf')
                for i in range(9):
                    if board[i] == ' ':
                        board[i] = computer_symbol
                        score = min_max(False)
                        board[i] = ' '
                        best_score = max(score, best_score)
                return best_score
            else:
                best_score = float('inf')
                for i in range(9):
                    if board[i] == ' ':
                        board[i] = playersymbol
                        score = min_max(True)
                        board[i] = ' '
                        best_score = min(score, best_score)
                return best_score
        
        def computer_move():
            best_score = -float('inf')
            move = None
            for i in range(9):
                if board[i] == ' ':
                    board[i] = computer_symbol
                    score = min_max(False)
                    board[i] = ' '
                    if score > best_score:
                        best_score = score
                        move = i
            return move
        while True:
            print_board()
            if current_player == playersymbol:
                try:
                    move = int(input(f"{name}, enter your move (0-8): "))
                    if move < 0 or move >= 9 or board[move] != ' ':
                        print("\nInvalid move. Try again.")
                        continue
                except ValueError:
                    print("\nInvalid input. Please enter a number between 0 and 8.")
                    continue
            else:
                move = computer_move()
                print(f"Computer chose position {move}.")
            board[move] = current_player
            
            if check_winner_for(current_player):
                print_board()
                if current_player == playersymbol:
                    print(f"\n🎉🎉{name} wins!")
                    player_wins += 1
                else:
                    print(f"\n🤖Computer wins! Better luck next time, {name}.")
                    computer_wins += 1
                break
            if is_full():
                print_board()
                print("\nIt's a tie 🫨!")
                break
            
            if current_player == playersymbol:
                current_player = computer_symbol
            else:
                current_player = playersymbol
        game_count += 1
        print(f"Game Count: {game_count}")
        print(f"{name} Wins: {player_wins}")
        print(f"Computer Wins: {computer_wins}")
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

        