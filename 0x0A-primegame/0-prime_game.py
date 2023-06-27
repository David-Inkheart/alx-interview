#!/usr/bin/python3
""" Solving the prime game """


def isWinner(x, nums):
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
    if n < 2:
        return 0

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return sum(primes)


def prime_num(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
