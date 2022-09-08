#!/usr/bin/python3
""" triangle fn """

def pascal_triangle(n):
    """ Function that returns a list of lists
        of integers representing the Pascal’s
        triangle of n """
    x = []
    if n == 1:
        return [1]
    else:
        for i in range(n):
            l = [1]
            if x:
                last = x[-1]
                l.extend([sum(pair) for pair in zip(last, last[1:])])
                l.append(1)
            x.append(p)
    return(x)