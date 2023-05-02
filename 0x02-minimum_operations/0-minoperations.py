#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n: int) -> int:
    """Method that calculates the fewest number of operations needed to
    resultin exactly n H characters in the file.
    """
    # If n is impossible to achieve, return 0. File already has 1 H
    if n <= 1:
        return 0

    # Find the smallest factor of n starting from 2
    for fact in range(2, n + 1):
        if n % fact == 0:
            # Return fact + the number of operations needed to get the
            # remaining  `n / fact`` Hs
            return fact + minOperations(int(n / fact))
