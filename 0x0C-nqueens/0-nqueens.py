#!/usr/bin/python3
"""
The N-Queens problem is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other
"""
import sys
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = eval(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if (N < 4):
    print('N must be at least 4')
    exit(1)
Grid = [[0]*N for _ in range(N)]
Nq = [N]
solution = []


def attack(i, j):
    """
    Check if a queen placed at (row, col) is under attack from any other queens
    """
    for k in range(N):
        if Grid[i][k] == 1 or Grid[k][j] == 1:
            return True
    for k in range(N):
        for z in range(N):
            if (k + z == i + j) or (k - z == i - j):
                if Grid[k][z] == 1:
                    return True
    return False


def Nqueens(n, x):
    """
    Place queens on the chessboard by backtracking
    """
    for i in range(x, N):
        for j in range(N):
            if (not(attack(i, j))) and (Grid[i][j] != 1):
                Grid[i][j] = 1
                Nq[0] = Nq[0] - 1
                Nqueens(n - 1, i + 1)
                if Nq[0] == 0:
                    position()
                Grid[i][j] = 0
                Nq[0] = Nq[0] + 1
    return False


def reset(N):
    """
    Reset the chessboard to all zeros
    """
    for k in range(N):
        for z in range(N):
            Grid[k][z] = 0


def validate(N):
    """
    Validate the solution by checking if the number of queens placed is equal to N
    """
    suma = 0
    store = []
    for k, i in enumerate(Grid):
        if 1 in i:
            store.append([k, i.index(1)])
            suma += 1
    if suma == N:
        return store
    else:
        return []


def position():
    """
    Store a valid solution if it doesn't already exist in the list of solutions
    """
    x = validate(N)
    if len(x) == N and x not in solution:
        print(x)
        solution.append(x)


Nqueens(N, 0)
