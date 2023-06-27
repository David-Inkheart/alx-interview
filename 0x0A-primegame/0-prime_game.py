#!/usr/bin/python3
""" Solving the prime game

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

def isWinner(x, nums):
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    def get_max_prime(primes, num):
        while num >= 0 and not primes[num]:
            num -= 1
        return num

    wins = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        n = nums[i]
        primes = sieve(n)
        max_prime = get_max_prime(primes, n)
        total_moves = max_prime // 2 + 1
        if total_moves % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None """


def isWinner(x, nums):
    def filter_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    def optimus_prime(primes, num):
        while num >= 0 and not primes[num]:
            num -= 1
        return num

    scores = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        n = nums[i]
        primes = filter_primes(n)
        max_prime = optimus_prime(primes, n)
        total_moves = max_prime // 2 + 1
        if total_moves % 2 == 0:
            scores['Ben'] += 1
        else:
            scores['Maria'] += 1

    if scores['Maria'] > scores['Ben']:
        megatron = 'Maria'
    elif scores['Maria'] < scores['Ben']:
        megatron = 'Ben'
    else:
        megatron = None

    return megatron
