import sys

def is_safe(board, row, col, N):
    # check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
 
    # check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False
 
    return True

def solve_n_queens(board, row, N):
    # base case: if all rows have been placed, a solution has been found
    if row == N:
        print_solution(board, N)
        return True
 
    # try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            # recursively try placing the remaining queens
            if solve_n_queens(board, row+1, N):
                return True
            # backtrack: unplace the queen and try a different placement
            board[row][col] = 0
 
    # if no placement is possible, return False
    return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
 
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
 
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
 
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0, N):
        print("No solution found")

if __name__ == "__main__":
    main()
