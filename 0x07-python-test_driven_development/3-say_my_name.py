#!/usr/bin/python3
"""A function that prints out a name

Attributes:
    say_my_name: function that prints my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that printss out a name

    Args:
        first_name (string): A name.
        last_name (string): An optional name.

    Raises:
        TypeError: If values are not strings.

    Returns:
        string: The full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
