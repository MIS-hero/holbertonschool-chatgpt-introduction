#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: factorial
    ------------------
    Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer for which the factorial is computed.

    Returns:
        int: The factorial of the number n.
             If n is 0, returns 1 (by definition).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command-line argument and compute factorial
f = factorial(int(sys.argv[1]))
print(f) 