#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding
LOGIC:
each integer in the list must have a value between 0 and 255, inclusive.
But, this is not enough. The specific patterns of a UTF-8 Binary
also must be matched

For a single point that can be converted to single byte, it must be:
1-byte, containing 8-bits and starting with '0', i.e  '0xxxxxxx'= 8bits
2-bytes containing 8-bits each in format '110xxxxx' for the first and
'10xxxxxx' for the second byte... so... 110xxxxx10xxxxxx = 16bits
3-bytes 1110xxxx10xxxxxx10xxxxxx = 24bits
4-bytes 11110xxx10xxxxxx10xxxxxx10xxxxxx = 32bits

so, to check that a number is properly encoded as a utf-8,
then check that it has a valid binary utf-8 format as prescribed above.

bit shifting is employed to make this concise and straightforward. i.e.
byte >> 5 shifts the bits of byte 5 positions to the right.
This is used to check the first 3 bits of byte to identify if it
represents the start of a 2-byte character.
"""


def validUTF8(data) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    if data is None:
        return False

    remaining_bytes = 0

    for byte_value in data:
        if remaining_bytes == 0:
            # This byte should start a new character
            if byte_value >> 5 == 0b110:
                # 2-byte character: first byte starts with '110'
                remaining_bytes = 1
            elif byte_value >> 4 == 0b1110:
                # 3-byte character: first byte starts with '1110'
                remaining_bytes = 2
            elif byte_value >> 3 == 0b11110:
                # 4-byte character: first byte starts with '11110'
                remaining_bytes = 3
            elif byte_value >> 7 == 0b1:
                # Invalid character, should start with '0'
                return False
        else:
            # This byte should be part of an existing character
            if byte_value >> 6 != 0b10:
                # Invalid continuation byte, should start with '10'
                return False
            remaining_bytes = remaining_bytes - 1
    # All bytes have been checked and no incomplete character is left
    return remaining_bytes == 0
