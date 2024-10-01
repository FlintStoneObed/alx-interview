#!/usr/bin/python3

def isWinner(x, nums):
    """Determines the winner of each game."""
    
    if not nums or x < 1:
        return None
    
    # Step 1: Find the maximum number in the nums list
    max_n = max(nums)
    
    # Step 2: Use the Sieve of Eratosthenes to find all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False
    
    # Step 3: Precompute the number of prime removals (moves) for each n
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + primes[i]
    
    # Step 4: Determine who wins each game based on the number of moves
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the number of prime moves is odd
        else:
            ben_wins += 1  # Ben wins if the number of prime moves is even
    
    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
