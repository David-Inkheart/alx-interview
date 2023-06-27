# Prime Game

Maria and Ben are playing a game where they take turns choosing a prime number from a set of consecutive integers starting from 1 up to and including n. The chosen number and its multiples are then removed from the set. The player who cannot make a move loses the game.

This program determines the winner of each game given the number of rounds played and the values of n for each round. Assuming Maria always goes first and both players play optimally, the program returns the name of the player who won the most rounds. If the winner cannot be determined, it returns None.

## Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner of each game played.

    Args:
      x (int): The number of rounds.
      nums (list): An array of n for each round.

    Returns:
      str: Name of the player who won the most rounds.
           If the winner cannot be determined, returns None.
    """
```

## Constraints

- The values of n and x will not exceed 10,000.
- No external packages are allowed to be imported.

## Example

```python
x = 3
nums = [4, 5, 1]
print("Winner: {}".format(isWinner(x, nums)))
```

Output:
```
First round: 4
Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose

Second round: 5
Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose

Third round: 1
Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins
```

The program output will be:
```
Winner: Ben
```