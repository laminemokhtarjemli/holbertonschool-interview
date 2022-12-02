#!/usr/bin/python3

'''
challenge of placing N non-attacking queens
'''
from sys import argv

def NQueen(cell :list) -> bool:
    
    row = len(cell) - 1
    diff = 0
    for indx in range(0, row):
        diff = cell[indx] - cell[row]
        if diff < 0:
            diff *= -1
            if diff == 0 or diff == row - indx:
                return False
    return True

def solve(dim: int, rowboard: int, cell:list, outcome: list):

    if rowboard == dim:
        print(outcome)
    else:
        for col in range(0, dim):
            cell.append(col)
            outcome.append([rowboard, col])
            if (NQueen(cell)):
                solve(dim, rowboard + 1, cell, outcome)
            cell.pop()
            outcome.pop()

try:
    N = int(argv[1])
except BaseException:
    print('Must be a NUMBER => N')
    exit(1)
if N < 4:
    print('N must be higher than 4')
    exit(1)
else:
    outcome = []
    cell = 0
    solve(int(N), cell, outcome)