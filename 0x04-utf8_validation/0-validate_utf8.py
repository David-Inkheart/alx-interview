#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding
LOGIC:
In UTF-8 encoding, each character can be represented by 1 to 4 bytes,
with each byte having a value between 0 and 255 (i.e., a single byte
can represent 2^8 = 256 distinct values). Therefore, in a valid UTF-8 encoding
each integer in the list must have a value between 0 and 255, inclusive.

If a value greater than 255 is encountered in a list of integers representing
a UTF-8 encoding, it is considered an invalid encoding, since the byte value
is outside the range of valid byte values in UTF-8.

But, this is not enough. The specific patterns of a UTF-8 Binary
also must be matched
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    return all(0 <= item <= 255 for item in data)
