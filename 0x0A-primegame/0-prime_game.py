#!/usr/bin/python3
""" Solving the prime game """


def remove_multiples(num, lst):
    """
    Removes multiples of a given number from a list
    """
    new_lst = [item for item in lst if item % num != 0]
    return new_lst


def is_prime(number):
    """
    Checks if a number is prime
    """
    if number == 1:
        return False
    for j in range(2, int(number ** 0.5) + 1):
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
            target = remove_multiples(i, target)
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
    # if not nums or x < 1:
    #     return None
    # if any(num <= 0 for num in nums):
    #     return None
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
