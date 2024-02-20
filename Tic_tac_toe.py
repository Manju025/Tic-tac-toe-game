def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_board(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter your row(0, 1, 2): "))
        col = int(input("Enter your column(0, 1, 2): "))

        if check_board(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif check_board(board):
            print_board(board)
            print("It is tie!")
            break

        player = "O" if player == "X" else "X"
if __name__ == "__main__":
    tic_tac_toe()