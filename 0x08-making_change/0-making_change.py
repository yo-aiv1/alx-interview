#!/usr/bin/python3
"""08 making change"""


def makeChange(coins, total):
    """
    get the the fewest number of coins needed to meet a given amount
    """
    coins.sort()
    TotalCoins = [0] * (total + 1)

    for i in range(1, total + 1):
        mini = float('inf')

        for coin in coins:
            diff = i - coin
            if diff < 0:
                break

            mini = min(mini, TotalCoins[diff] + 1)
        TotalCoins[i] = mini

    if TotalCoins[total] < float('inf'):
        return TotalCoins[total]
    return -1
