#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change2').makeChange

print(makeChange([1, 4, 5], 8))
print(makeChange([1, 4, 5], 10))
print(makeChange([1, 4, 5, 6, 7], 10))
print(makeChange([3, 4, 5], 8))
