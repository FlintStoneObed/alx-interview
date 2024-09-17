#!/usr/bin/python3
"""Module for calculating the fewest coins needed to make a given amount"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of the coin denominations.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be met, return -1.
    """
    if total <= 0:
        return 0

    # Initialize a list to track the minimum coins required for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
