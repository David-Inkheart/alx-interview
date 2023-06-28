#!/usr/bin/python3
""" Solving the prime game """


# def isWinner(x, nums):
#     """
#     Determines the winner of each game played.

#     Args:
#       x (int): The number of rounds.
#       nums (list): An array of n for each round.

#     Returns:
#       str: Name of the player who won the most rounds.
#            If the winner cannot be determined, returns None.
#     """
#     if not nums or x < 1:
#         return None

#     wins = 0

#     for n in nums:
#         primes = c_primes(n)
#         if primes % 2 == 1:
#             wins += 1

#     if wins % 2 == 0:
#         return "Ben"
#     return "Maria"


# def c_primes(n):
#     """
#     Counts the number of prime numbers up to and including n.

#     Args:
#       n (int): The upper limit.

#     Returns:
#       int: The count of prime numbers.
#     """
#     if n < 2:
#         return 0

#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False

#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False

#     return sum(primes)


# def prime_num(num):
#     """
#     Checks if a number is prime.

#     Args:
#       num (int): The number to check.

#     Returns:
#       bool: True if the number is prime, False otherwise.
#     """
#     if num < 2:
#         return False

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False

#     return True

def remove_multiples(num, targets):
    """
    Removes multiples of a given number from a list
    """
    for i in targets:
        if i % num == 0:
            targets.remove(i)
    return targets


def is_prime(number):
    """
    Checks if a number is prime
    """
    if number == 1:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True


def count_primes(nums):
    """
    Counts the number of primes in a given set
    """
    counter = 0
    target = list(nums)
    for i in range(1, len(target) + 1):
        if is_prime(i):
            counter += 1
            target.remove(i)
            target = remove_multiples(i, target)
        else:
            pass
    return counter


def isWinner(x, nums):
    """
    Maria and Ben are playing a game.Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its
    multiples from the set.
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """
    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = count_primes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
