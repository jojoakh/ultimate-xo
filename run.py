# Create a 4x4 tic tac toe board
board = [[" " for _ in range(4)] for _ in range(4)]

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

display_board(board)
display_rules()