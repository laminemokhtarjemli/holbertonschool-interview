#!/usr/bin/python3
import sys

def n_queens(n):
    if n < 4:
        print("N must be at least 4")
        return
    solutions = []
    def backtrack(board, cols, diag1, diag2, row):
        if row == n:
            solutions.append(board)
            return
        for col in range(n):
            if col not in cols and row - col not in diag1 and row + col not in diag2:
                backtrack(board + [(row, col)], cols + [col], diag1 + [row - col], diag2 + [row + col], row + 1)
    backtrack([], [], [], [], 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)
    print(n_queens(n))
