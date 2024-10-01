#!/usr/bin/python3
"""
This module defines the function isWinner
for determining the winner between Maria and Ben
in a game where they pick prime numbers and remove them
and their multiples from a set of consecutive integers.
"""


def isWinner(x: int, nums: list) -> str:
    """
    Determines the winner after x rounds of the game.
    
    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the upper bounds for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
             If there is no clear winner, return None.
    """
    
    if x < 1 or not nums:
        return None
    
    # Find the maximum value of n across all rounds
    max_n = max(nums)
    
    # Step 1: Create a sieve to mark prime numbers up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False
    
    # Step 2: Precompute the number of prime moves for each value of n
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + primes[i]
    
    # Step 3: Count wins for Maria and Ben based on the number of prime moves
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1  # Odd prime moves mean Maria wins
        else:
            ben_wins += 1  # Even prime moves mean Ben wins
    
    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
