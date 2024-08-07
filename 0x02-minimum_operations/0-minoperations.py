#!/usr/bin/python3
'''Interview Challenge module '''

def minOperations(n):
    '''
    Finds the minimum number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The number of H characters to achieve.

    Returns:
        int: The minimum number of operations needed. If n is impossible to achieve, return 0.
    '''
    # Check if n is a non-negative integer and not equal to 1
    if not isinstance(n, int) or n < 0 or n == 1:
        return 0

    # Initialize variables
    var = 1
    count = 0
    dup = 0

    # Loop until var is greater than or equal to n
    while var < n:
        # If n is not divisible by var, increment var by dup and increment count by 1
        if n % var != 0:
            var += dup
            count += 1
        # If n is divisible by var, set dup to var, increment var by dup, and increment count by 2
        else:
            dup = var
            var += dup
            count += 2

    # Return count if var is equal to n, otherwise return 0
    return (count if var == n else 0)

