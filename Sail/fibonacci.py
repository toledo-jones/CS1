def fib(n):
    """
    The function returns the number in Fibonacci sequence that is at the
    position provided by the argument. If the argument is a negative integer or
    some other type the function returns None.
    Examples:
    0 -> 0
    1 -> 1
    2 -> 1  (0 + 1)
    3 -> 2  (1 + 1)
    4 -> 3  (1 + 2)
    5 -> 5  (2 + 3)
    6 -> 8  (3 + 5)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :param n: integer
    :return: integer
    """
    # Check if the input is less than 0 or not an integer.
    # Return None if any of the above is True.
    if n < 0 or type(n) != int:
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1 * v1 +calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def test_fib() -> None:
    """
    This is a suite of tests for the fib function.
    :return: None
    """
    assert fib(1) == 1
    assert fib(0) == 0
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

