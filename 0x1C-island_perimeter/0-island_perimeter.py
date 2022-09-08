#!/usr/bin/python3
"""
This module contains the function island_perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    p = 0
    for x in range(len(grid)):
        for a in range(len(grid[x])):
            if grid[x][a] == 1:
                if x == 0 or grid[x - 1][a] == 0:
                    p += 1
                if a == 0 or grid[x][a - 1] == 0:
                    p += 1
                if x == len(grid) - 1 or grid[x + 1][a] == 0:
                    p += 1
                if a == len(grid[x]) - 1 or grid[x][a + 1] == 0:
                    p += 1
    return p