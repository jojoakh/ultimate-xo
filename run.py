import os
import random

# Define the initial board state
board = [[" " for _ in range(4)] for _ in range(4)]

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
    cell_num = 1
    for row in range(4):
        for col in range(4):
            if board[row][col] == " ":
                print(f"{cell_num:2}", end=" | ")
            else:
                print(f"{board[row][col]:2}", end=" | ")
            cell_num += 1
        print()
        if row < 3:
            print("-" * 19)

# Function to display the rules of the game
def display_rules():
    print("\nTic Tac Toe Rules:\n")
    print("1. The game is played on a 4x4 grid.")
    print("2. Players take turns placing their marks ('X' or 'O') in empty cells.")
    print("3. The objective is to be the first player to get four of your marks in a row,")
    print("   horizontally, vertically, or diagonally on a 4x4 grid.")
    print("4. Players cannot overwrite their opponent's mark.")
    print("5. The first player usually starts with 'X'.")
    print("6. The game ends when a player achieves a winning condition or the board is full (draw).")
    print("7. Have fun and enjoy the game!\n")

# Function to display the welcome message
def welcome_message():
    print(title)
    print("Please select an option to proceed:\n")
    print("1. Rules\n")
    print("2. Start Game\n")
    print("3. Exit\n")

# Function to check for a win
def check_win(board, mark):
    # Check rows, columns, and diagonals for a win
    for i in range(4):
        if all(board[i][j] == mark for j in range(4)) or all(board[j][i] == mark for j in range(4)):
            return True
    if all(board[i][i] == mark for i in range(4)) or all(board[i][3-i] == mark for i in range(4)):
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

# Function for computer's move
def computer_move(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

# Function to convert a cell number to row and column indices
def cell_to_indices(cell_num):
    row = (cell_num - 1) // 4
    col = (cell_num - 1) % 4
    return row, col

# Main function to control the flow of the game
def main():
    while True:
        welcome_message()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_rules()
        elif choice == "2":
            board = [[" " for _ in range(4)] for _ in range(4)]  # Reset the board
            
           

# Call the main function to start the game
main()
