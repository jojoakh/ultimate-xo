import os
import random


# Define the initial board state with numbers 1 to 16
def initial_board():
    """
    Initialize the game board with numbers from 1 to 16 in a 4x4 grid.
    A 4x4 nested list representing the game board.
    Each cell contains a string with a number from 1 to 16.
    """
    return [[str(i * 4 + j + 1) for j in range(4)] for i in range(4)]


# Define the title art
title = r"""
Hello!

////////////////////////////////////////////////////////////////////////////
//  __        __   _                            _          _____ _        //
//  \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |_   _(_) ___   //
//   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | | | |/ __|  //
//    \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | | | | (__   //
//   __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    |_| |_|\___|  //
//  |_   _|_ _  ___  |_   _|__   ___   / ___| __ _ _ __ ___   ___         //
//    | |/ _` |/ __|   | |/ _ \ / _ \ | |  _ / _` | '_ ` _ \ / _ \        //
//    | | (_| | (__    | | (_) |  __/ | |_| | (_| | | | | | |  __/        //
//    |_|\__,_|\___|   |_|\___/ \___|  \____|\__,_|_| |_| |_|\___|        //
////////////////////////////////////////////////////////////////////////////
"""


# Function to display the board with numbers
def display_board(board):
    """
    Display the current state of the game board
    with numbers in a 4x4 grid format.
    """
    for row in board:
        print(f"|{row[0].center(5)}|"
              f"{row[1].center(5)}|"
              f"{row[2].center(5)}|"
              f"{row[3].center(5)}|")
        print(" _____ _____ _____ _____ ")
    print()


# Function to display the rules of the game
def display_rules():
    """
    Print the rules of the game.
    """
    print("\nTic Tac Toe Rules:\n")
    print("1. The game is played on a 4x4 grid.")
    print("2. Players take turns placing their marks in empty cells.")
    print("3. The objective is to be the first to get four marks in a row,")
    print("   horizontally, vertically, or diagonally on a 4x4 grid.")
    print("4. Players cannot overwrite their opponent's mark.")
    print("5. The first player usually starts with 'X'.")
    print("6. The game ends when a player wins or the board is full (draw).")
    print("7. Have fun and enjoy the game!\n")


# Function to display the welcome message
def welcome_message():
    """
    Print the welcome message with the title
    and initial options for the player.
    """
    print(title)
    print("Please select an option to proceed:\n")
    print("1. Rules\n")
    print("2. Start Game\n")
    print("3. Exit\n")


# Function to check for a win  
def check_win(board, mark):
    """
    Check if a player has won the game
    """
    for i in range(4):
        if (all(board[i][j] == mark for j in range(4)) or
                all(board[j][i] == mark for j in range(4))):
            return True
    if (all(board[i][i] == mark for i in range(4)) or
            all(board[i][3-i] == mark for i in range(4))):
        return True
    return False


# Function to check for a draw
def check_draw(board):
    """
    Check if the game is a draw when all the cells are filled up.
    """
    return all(all(cell in ["X", "O"] for cell in row) for row in board)


# Function for computer's move
def computer_move(board):
    """
    Perform the computer's move on the board.
    """
    empty_cells = [(i, j) for i in range(4) for j in range(4)
                   if board[i][j] not in ["X", "O"]]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"


# Function to convert a cell number to row and column indices
def cell_to_indices(cell_num):
    """
    Convert a cell number (1-16) to row and column indices in the game board.
    """
    row = (cell_num - 1) // 4
    col = (cell_num - 1) % 4
    return row, col


# Function to replay the game
def replay():
    """
     Ask the player if they want to play again.
    """
    while True:
        choice = input("\nWant to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("\nInvalid choice. Please enter 'yes' or 'no'.")


# Function to get a valid username
def get_username(player_num):
    """
    Prompt the player to enter a valid username
    with 3 to 8 letters.
    """
    while True:
        username = input(f"\nPlayer {player_num} enter username "
                         "(3-8 letters): ").strip()
        if 3 <= len(username) <= 8 and username.isalpha():
            return username
        else:
            print("Invalid username. Enter a username with 3 to 8 letters.")


# Main function to control the flow of the game
def main():
    """
    Main function to start and control the flow of the Tic Tac Toe game.
    """
    welcome_message()
    while True:
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_rules()
            continue  # Go back to the main menu after displaying rules
        elif choice == "2":
            while True:
                board = initial_board()  # Initialize the board with numbers

                print("\nSelect game mode:")
                print("1. Two Players")
                print("2. Play with Computer")
                game_mode = input("\nEnter your choice: ").strip()

                if game_mode == "1":
                    player1 = get_username(1)
                    player2 = get_username(2)
                elif game_mode == "2":
                    player1 = get_username(1)
                    player2 = "Computer"
                else:
                    print("\nInvalid choice. Please select 1 or 2.")
                    continue

                current_player = "X"
                while True:
                    os.system('clear')  # Clear the console
                    display_board(board)
                    if (game_mode == "1" or
                            (game_mode == "2" and current_player == "X")):

                        if current_player == "X":
                            player_name = player1
                        else:
                            player_name = player2

                        valid_move = False
                        while not valid_move:
                            try:
                                cell_num = int(input(
                                    f"\n{player_name} ({current_player}), "
                                    "enter number (1-16): ").strip())
                                if cell_num < 1 or cell_num > 16:
                                    print("\nNumber out of range.")
                                    print("Enter a number between 1 and 16.")
                                    continue

                                row, col = cell_to_indices(cell_num)
                                if board[row][col] in ["X", "O"]:
                                    print("\nCell already occupied.")
                                    print("Please choose another cell.")
                                    continue

                                valid_move = True
                            except ValueError:
                                print("\nInvalid input.")
                                print("Enter a valid number between 1 and 16.")
                                continue

                        board[row][col] = current_player
                        if check_win(board, current_player):
                            os.system('clear')  # Clear the console
                            display_board(board)
                            print(f"\nCongratulation {player_name}!")
                            print(f"\nYou win!\n")
                            break
                        elif check_draw(board):
                            os.system('clear')  # Clear the console
                            display_board(board)
                            print("\nIt's a draw!\n")
                            break
                        current_player = "O" if current_player == "X" else "X"

                    else:
                        computer_move(board)
                        if check_win(board, "O"):
                            os.system('clear')  # Clear the console
                            display_board(board)
                            print("\nComputer wins!\n")
                            break
                        elif check_draw(board):
                            os.system('clear')  # Clear the console
                            display_board(board)
                            print("\nIt's a draw!\n")
                            break
                        current_player = "X"
                if not replay():
                    print("\nThank you for playing! Goodbye!\n")
                    return
        elif choice == "3":
            print("\nThank you for playing! Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.\n")


# Call the main function to start the game
main()
