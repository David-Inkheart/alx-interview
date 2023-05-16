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

bit shifting and masking is employed to make this concise and
straightforward
"""


def validUTF8(data) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    if data is None:
        return False

    remaining_bytes = 0

    for byte_value in data:
        mask = 1 << 7

        if remaining_bytes == 0:
            # This byte should start a new character
            while byte_value & mask:
                # Count the number of leading '1' bits to determine the
                # number of bytes in the character
                remaining_bytes += 1
                mask >>= 1

            if remaining_bytes == 0:
                # No leading '1' bit found, move to the next byte
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                # Invalid number of bytes for a character (must be 2-4)
                return False
        else:
            # This byte should be part of an existing character
            if byte_value >> 6 != 0b10:
                # Invalid continuation byte, it should start with '10'
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
