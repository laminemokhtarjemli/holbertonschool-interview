#!/usr/bin/python3
"""script that uses backtracking to solve the N-Queens problem. 
    The N-Queens problem is the task of placing N chess queens on an
    NxN chessboard"""
import sys


def n_queens(x, z, board):
        """
        The N-Queens problem is the task of placing N chess
        queens on an NxN chessboard so that no two queens 
        threaten each other.

        Parameters: The x argument represents the size of the chessboard
        and the number of queens to be placed
        """
        for i in range(x):
            hold = 0
            for q in board:
                if i == q[1]:
                    hold = 1
                    break
                if z - i == q[0] - q[1]:
                    hold = 1
                    break
                if i - q[1] == q[0] - z:
                    hold = 1
                    break
            if hold == 0:
                board.append([z, i])
                if z != x - 1:
                    n_queens(x, z + 1, board)
                else:
                    print(board)
                del board[-1]


def main():
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        try:
            n = int(sys.argv[1])
        except Exception:
            print('N must be a number')
            sys.exit(1)
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        n_queens(n, 0, [])

if __name__ == '__main__':
        main()
