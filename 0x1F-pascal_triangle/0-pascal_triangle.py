#!/usr/bin/python3
"""
function that returns a list of lists of integers
"""

def pascal_triangle(n):
    """
    function that returns a list of lists of ints
    """
    res = []
    end = []

    if n <= 0:
        return []

    else: 
        for i in range(1, n + 1):
            k = 1
            for j in range(1, i + 1):
                res.append(k)

                k = k * (i - j) // j 

            end.append(res)
            res = []

    return end