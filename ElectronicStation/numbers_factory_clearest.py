"""
Return the smallest number such that the products of its digits equal a given number.
"""
import functools

def checkio(number):
    """
    Return the smallest integer such that the product of its digits equal 'number'.
    If this is not possible, return zero.
    """
    # Special case for one to keep the logic simpler (and zero, as an early out).
    if number <= 1:
        return number

    # Factor number into factors in the range [2, 9] (inclusive)
    factors = []
    for d in reversed(range(2, 10)):
        while number > 1 and not number % d:
            number //= d
            factors.append(d)

    # If the number has not been completely factored, it must have prime
    # factors larger than seven.  In this case, it's impossible to factor
    # with digits, so return zero.
    if number > 1:
        return 0

    # Combine the factors back into a single integer.
    # Use reversed so that smaller digits come first.
    return functools.reduce(lambda a, b: 10 * a + b, reversed(factors))
