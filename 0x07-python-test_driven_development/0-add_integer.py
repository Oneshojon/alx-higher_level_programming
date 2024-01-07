#!/usr/bin/python3
"""Function that adds 3 numbers

Artributes:
   add_integer: adds two numbers
"""


def add_integer(a, b=98):
    """
    A function to add two digits.

    Args:
        a (int): a number
        b (int): Optional value.

    Returns:
        int: Sum of a and b.

    Raise:
        TypeErrot: If values of a and b are not integers.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
