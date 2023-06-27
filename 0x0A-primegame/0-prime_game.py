#!/usr/bin/python3
""" solving the prime game """


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
    if not nums or x < 1:
        return None

    wins = 0

    for n in nums:
        primes = c_primes(n)
        if primes % 2 == 1:
            wins += 1

    if wins % 2 == 0:
        return "Ben"
    return "Maria"


def c_primes(n):
    """
    Counts the number of prime numbers up to and including n.

    Args:
      n (int): The upper limit.

    Returns:
      int: The count of prime numbers.
    """
    primes = 0

    for num in range(2, n + 1):
        if prime_num(num):
            primes += 1

    return primes


def prime_num(num):
    """
    Checks if a number is prime.

    Args:
      num (int): The number to check.

    Returns:
      bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
