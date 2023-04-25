## [0. Lockboxes](./0-lockboxes.py)

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: def `canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

```
carrie@ubuntu:~/0x01-lockboxes$
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

### Major concept applied:

The major concept applied in the final code is using a breadth-first search algorithm to check if all the boxes can be unlocked. This is done by starting with the first box (index 0), adding its keys to a set of available keys, and then checking each key in the set to see if it can unlock a new box. If a key can unlock a new box, the index of that box is added to a set of opened boxes, and its keys are added to the set of available keys. This process continues until all boxes have been opened or all available keys have been tried and no new boxes can be opened

This approach ensures that each box is only checked once, and the algorithm will terminate early if all boxes have been opened. It also avoids the need to generate a separate list of all available box indices, as I did in an earlier version, as the set of opened boxes can be used instead.
