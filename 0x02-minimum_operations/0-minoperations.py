#!/usr/bin/python3

"""
calculates the fewest number of operations
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ Calculates the fewest number of operations
    to result in exactly n H characters in the file.
    Args:
        n (int): Number of H characters to reach.
    Returns:
        (int): The fewest number of operations
    """
    if n <= 1:
        return 0
    else:
        i = 2
        operations = 0
        while i <= n:
            if n % i == 0:
                operations += i
                n = n / i
            else:
                i += 1
        return operations
