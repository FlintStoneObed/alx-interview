#!/usr/bin/python3
"""Module for determining the fewest coins needed to meet a given total amount"""

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

    # Create an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin and compute the minimum coins needed for each amount
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result for the target total or -1 if it can't be met
    return dp[total] if dp[total] != float('inf') else -1
