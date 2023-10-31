import math

def is_prime(n):
    """
    Check if this number is prime or not.

    Args:
        n (int) is the number.

    Returns:
        bool: True if the number is prime, otherwise it returns False.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(1)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True