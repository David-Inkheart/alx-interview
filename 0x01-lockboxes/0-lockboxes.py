#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""
""" LOGIC: First box is open, it should contain the a number which is the index
(position on the list) of the next box or another box and so on,
until all boxes are opened. So, I need to compare contents of
boxes with available indexes.

for example boxes = [[1], [2], [3], [4], []]. Total available index are:
0, 1, 2, 3, 4. note how the content of each box match those index,
hence this would be TRUE that all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """"function to unlock boxes"""

    """keep track of unique keys and unlocked boxes"""
    keyRing = set(boxes[0])
    unlockedBoxes = {0}

    """loop until no more boxes can be unlocked"""
    while True:
        """keep track of how many boxes were unlocked in this iteration"""
        b_unlocked = 0
        """try to unlock remaining boxes"""
        for i in range(len(boxes)):
            if i not in unlockedBoxes and i in keyRing:
                unlockedBoxes.add(i)
                keyRing.update(boxes[i])
                b_unlocked += 1
        """if no boxes were unlocked, we're done"""
        if b_unlocked == 0:
            break

    """check if all boxes were unlocked"""
    return len(unlockedBoxes) == len(boxes)
