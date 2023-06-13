#!/bin/bash/python3
"""Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total."""


def makeChange(coins, total):
    """
    return least qty of coins to make change out of total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    c_qty = 0
    max_coin = coins[0]

    for coin in coins:
        if coin <= total:
            c_qty += total // coin
            """print("{} / {} = {}, qty of coins changed so far: {}".format(
                  total, coin, (total // coin), c_qty))"""
            total %= coin
            """print("{} / {} = {}, qty of coins changed so far: {}".format(
                  total, coin, (total // coin), c_qty))"""
            if coin == max_coin:
                max_coin = coins[coins.index(coin) + 1]

        if total == 0:
            return c_qty

    return -1
