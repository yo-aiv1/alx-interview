#!/usr/bin/python3
"""08 making change"""


def makeChange(coins, total):
    """
    get the the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
