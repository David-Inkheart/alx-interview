# Making Change

## 0. Change comes from within

Given a pile of `coins` of different values, determine the fewest number of `coins` needed to meet a given amount `total`.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

```
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
```

```
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```

### Logic and implementation:

- The logic behind this problem is to find the minimum number of coins needed to make change for a given amount of money.

### Implementation - [0-making_change.py](./0-making_change.py):
- After first using pseudo code to solve the problem, I decided on a precise and efficient solution.
-  This implementation iterates through the coin values in descending order and checks if each coin can be used to reduce the remaining total. If it can, it calculates the number of coins needed, updates the total, and checks if the total becomes zero. If the total becomes zero, it returns the accumulated coin count. If no combination of coins can meet the total, it returns -1.

### Alternative implementation - [0-making_change2.py](./0-making_change2.py):
- This implementation sorts the coin values in descending order and iterates through each coin. It checks if the current coin can be used to reduce the remaining total and updates the coin count accordingly. The code also tracks the maximum coin value and updates it when necessary.
- If the total becomes zero during the iteration, it returns the accumulated coin count. If no combination of coins can meet the total, it returns -1.

### Greedy Algorithm.

- Both implementations use a `greedy algorithm` to solve the problem.
  a greedy algorithm is an `algorithmic paradigm` that follows the `problem solving heuristic` of making the `locally optimal choice` at each stage with the hope of finding a `global optimum`. In this case, the `locally optimal choice is to use the largest coin value` that can be used to `reduce the remaining total`. This choice is made at each stage until the total becomes zero or no combination of coins can meet the total.