#!/usr/bin/python3
""" n queens """
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
if not isinstance(int(sys.argv[1]), int):
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])


def is_valid_state(state, n):
    return len(state) == n


def get_candidates(state, n):
    if not state:
        return range(n)

    position = len(state)
    candidates = set(range(n))
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        state_string = state_to_string(state)
        solutions.append(state_string)
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def solveNQueens(n):
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


def state_to_string(state):
    res = []

    for x, y in enumerate(state):
        res.append([x, y])
    return res


for solution in solveNQueens(n):
    print(solution)
