#!/bin/bash/python3
"""Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total."""


def makeChange(coins, total):
    """
    return least qty of coins to make change out of total
    """
    if total <= 0:
        return 0

    coin_list = sorted(coins, reverse=True)
    c_qty = 0

    for coin in coin_list:
        if coin <= total:
            c_qty += total // coin
            """print("{} / {} = {}, total coins so far: {}".format(
              total, coin, (total // coin), c_qty))"""
            total %= coin
            if total == 0:
                return c_qty

    return -1
