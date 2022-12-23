#!/usr/bin/python3

import sys

def is_valid(board, row, col):
    # Check this row on left side
    if 1 in board[row]:
        return False
    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def nqueens_helper(board, col):
    if col >= len(board):
        print_board(board, len(board))
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            result = nqueens_helper(board, col + 1)
            if result:
                return True
            board[i][col] = 0
    return False


def print_board(board, n):
    b = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b.append([i, j])
    print(b)


def nqueens(n):
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    nqueens_helper(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        exit(1)
    elif int(queens) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(queens))
