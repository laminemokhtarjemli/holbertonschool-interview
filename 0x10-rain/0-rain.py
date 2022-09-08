#!/usr/bin/python3
'''rain'''


def rain(walls=[]):
    """ self descriptive """
    if not walls or len(walls) == 0:
        return 0

    water_retained = 0
    n = len(walls)

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    right_max[n - 1] = walls[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(n):
        water_retained += min(left_max[i], right_max[i]) - walls[i]

    return water_retained