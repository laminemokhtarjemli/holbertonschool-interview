#!/usr/bin/python3
""" Nqueens """
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: chess_queens N")
    exit(1)
try:
        N = eval(sys.argv[1])
except Exception:
        print("N must be a number")
exit(1)
chess_board = [[0]*N for _ in range(N)]
remaining_queens = [N]
final_solutions = []
def check_attack(row, col):
    """
    Check if a queen placed at (row, col) is under attack from any other queens
    """
    for k in range(N):
        if chess_board[row][k] == 1 or chess_board[k][col] == 1:
            return True
    for k in range(N):
        for z in range(N):
            if (k + z == row + col) or (k - z == row - col):
                if chess_board[k][z] == 1:
                    return True
    return False
def find_queens(number_of_queens, current_row):
    """
    Place queens on the chessboard by backtracking
    """
    for i in range(current_row, N):
        for j in range(N):
            if not check_attack(i, j) and chess_board[i][j] != 1:
                chess_board[i][j] = 1
                remaining_queens[0] = remaining_queens[0] - 1
                find_queens(number_of_queens - 1, i + 1)
                if remaining_queens[0] == 0:
                    determine_position()
                chess_board[i][j] = 0
                remaining_queens[0] = remaining_queens[0] + 1
    return False
def clear_board(N):
    """
    Reset the chessboard to all zeros
    """
    for k in range(N):
        for z in range(N):
            chess_board[k][z] = 0
def validate_board(N):
    """
    Validate the solution by checking if the number of queens placed is equal to N
    """
    count = 0
    placed_queens = []
    for k, row in enumerate(chess_board):
        if 1 in row:
            placed_queens.append([k, row.index(1)])
            count += 1
    if count == N:
        return placed_queens
    else:
        return []
def determine_position():
    """
    Store a valid solution if it doesn't already exist in the list of solutions
    """
    positions = validate_board(N)
    if len(positions) == N and positions not in final_solutions:
        print(positions)
        final_solutions.append(positions)

find_queens(N, 0)
