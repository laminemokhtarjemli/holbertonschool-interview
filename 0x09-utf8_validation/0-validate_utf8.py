#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    a function that validates a UTF-8 encoding
    :param data: List of integers that will be validated
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    n_bytes = 0

    # Masks to check 1st and 2nd most significant bits
    mask_1 = 1 << 7
    mask_2 = 1 << 6
    for d in data:

        # Set to most significant bits
        mask = 1 << 7
        if n_bytes == 0:
            while mask & d:
                n_bytes += 1
                mask = mask >> 1

            # Condition for 1 byte characters
            if n_bytes == 0:
                continue

            # UTF8 must be 1 to 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if is part of existing UTF8
            if not (d & mask_1 and not (d & mask_2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
