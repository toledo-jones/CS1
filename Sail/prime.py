def is_prime(n):
    """
    The function returns True if the provided argument is an integer that is
    a prime number. It returns False otherwise.
    https://en.wikipedia.org/wiki/Prime_number
    :param n: integer
    :return: boolean
    """
    # If a given integer is greater than 1
    if n > 1 and type(n) == int:
        # Iterate from 2 to n / 2
        for i in range(2, int(n / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime.
            if n % i == 0:
                return False
        return True
    return False


def test_is_prime():
    """
    This is a suite of tests for the is_prime function.
    :return:
    """
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
