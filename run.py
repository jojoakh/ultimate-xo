# Create a 4x4 tic tac toe board
board = [[" " for _ in range(4)] for _ in range(4)]

# Function to display the board
def display_board(board):
    for row in range(4):
        print(" | ".join(board[row]))
        if row < 4:
            print("-" * 13)

display_board(board)