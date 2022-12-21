import sys

def solve(n, queens, xy_diffs, xy_sums):
    """
    Solves the N queens problem.

    Parameters:
    - n: the size of the chessboard
    - queens: a list of placed queens, represented as (x, y) tuples
    - xy_diffs: a set of x-y differences of placed queens to avoid attacks along diagonals
    - xy_sums: a set of x+y sums of placed queens to avoid attacks along diagonals
    """
    if n == len(queens):
        print(queens)
        return
    for y in range(n):
        x = len(queens)
        if (x-y) not in xy_diffs and (x+y) not in xy_sums:
            solve(n, queens + [(x, y)], xy_diffs + {x-y}, xy_sums + {x+y})

def main():
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solve(n, [], set(), set())

if __name__ == "__main__":
    main()
