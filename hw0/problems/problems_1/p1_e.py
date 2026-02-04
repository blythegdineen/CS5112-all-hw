from functools import reduce

def factorial_rec(n):
    """
    Returns the factorial of n using recursion.
    """
    if n < 2:
        factorial= 1
    else:
        factorial = n * factorial_rec(n-1)
    return factorial


def factorial_reduce(n):
    """
    Returns the factorial of n using functools reduce.
    """
    factorial = 1
    if n < 2:
        factorial= 1
    else:
        nums = list(range(1,n+1))
        factorial = reduce(lambda x, y: x * y, nums)
    return factorial
    