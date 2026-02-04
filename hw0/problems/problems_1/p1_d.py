from functools import reduce

def square_all(numbers):
    """
    Returns a list of squares of all numbers.
    """
    squares = []
    for n in numbers:
        squares.append(n*n)
    return squares

def filter_even(numbers):
    """
    Filters and returns only the even numbers from the list.
    """
    evens = []
    for n in numbers:
        if n%2==0:
            evens.append(n)
    return evens

def product_of_all(numbers):
    """
    Returns the product of all numbers in the list using reduce.
    """
    return reduce(lambda x, y: x * y, numbers)

