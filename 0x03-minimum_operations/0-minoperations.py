#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0

    number = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            number += i
            i = 1
        i += 1
    return number
