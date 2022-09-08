#!/usr/bin/python3
"""
    Check locked boxes
"""


def canUnlockAll(boxes):
    """
        Checks if the box can be opened
    """
    unlocked = [0]
    if len(boxes) == 0:
        return True
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked:
                if key < len(boxes):
                    unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True
    return False
