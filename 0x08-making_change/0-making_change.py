#!/usr/bin/python3
"""Module for determining the fewest coins needed to meet a given total amount."""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target amount to achieve using the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If the total cannot be met, return -1.
    """
    if total <= 0:
        return 0

    # Array to track the minimum coins needed for each value up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calculate the fewest coins needed for each value from 1 to total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
