import os


# Create a 4x4 tic tac toe board
board = [[" " for _ in range(4)] for _ in range(4)]
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

# Function to display the board
def display_board(board):
    for row in range(4):
        print(" | ".join(board[row]))
        if row < 4:
            print("-" * 13)

# function to display the rules of the game
def display_rules():
    print("Tic Tac Toe Rules:")
    print("1. The game is played on a 4x4 grid.")
    print("2. Players take turns placing their marks ('X' or 'O') in empty cells.")
    print("3. The objective is to be the first player to get four of your marks in a row,")
    print("   horizontally, vertically, or diagonally on a 4x4 grid.")
    print("4. Players cannot overwrite their opponent's mark.")
    print("5. The first player usually starts with 'X'.")
    print("6. The game ends when a player achieves a winning condition or the board is full (draw).")
    print("8. Have fun and enjoy the game!")

def welcome_message():
    print(title)
    print("Please select an option to begin:\n")
    print("1. Rules\n")
    

display_board(board)
display_rules()
welcome_message()