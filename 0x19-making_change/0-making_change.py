#!/usr/bin/python3
"""
function that change coin
"""


def makeChange(coins, total):
    """Fewest number of coins needed to meet a given amount total."""

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    stk = total
    m = 0
    ct = 0

    while (m < len(coins)):
        if stk == 0:
            return ct

        if coins[m] > stk:
            m += 1

        else:
            stk -= coins[m]
            ct += 1

    return -1
