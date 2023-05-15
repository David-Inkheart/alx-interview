#!/usr/bin/env python
"""

LOGIC:
In UTF-8 encoding, each character can be represented by 1 to 4 bytes,
with each byte having a value between 0 and 255 (i.e., a single byte
can represent 2^8 = 256 distinct values). Therefore, in a valid UTF-8 encoding
each integer in the list must have a value between 0 and 255, inclusive.

If a value greater than 255 is encountered in a list of integers representing
a UTF-8 encoding, it is considered an invalid encoding, since the byte value
is outside the range of valid byte values in UTF-8.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    some tests i am playing with for better understanding
    valid_utf8 = []
    for item in data:
        if item in range(0, 128):
            valid_utf8.append(item)
    return len(valid_utf8) == len(data)

    n_bytes = 0
    for byte in data:
        if n_bytes == 0:
            # This byte should start a new character
            if byte >> 5 == 0b110:
                # 2-byte character
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                # 3-byte character
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                # 4-byte character
                n_bytes = 3
            elif byte >> 7 == 0b1:
                # Invalid character, should start with 0
                return False
        else:
            # This byte should be part of an existing character
            if byte >> 6 != 0b10:
                # Invalid continuation byte, should start with 10
                return False
            n_bytes -= 1
    # All bytes have been checked and no incomplete character is left
    return n_bytes == 0
    """
    # The all() function is used to check if all the items
    # in the generator expression are True
    return all(0 <= item <= 255 for item in data)
