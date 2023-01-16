import sys

def is_valid(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def n_queens(board, row, n):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            n_queens(board, row + 1, n)
            board[row] = -1 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)
    elif n < 4:
        print("N must be at least 4")
        exit(1)
    board = [-1 for i in range(n)]
    n_queens(board, 0, n)
