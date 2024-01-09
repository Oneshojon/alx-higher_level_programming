#!/usr/bin/python3
"""Function to check if an object is an intanse of a specified class.

Attribute:
is_same_class: returns True or False
"""


def inherits_from(obj, a_class):
    """
    Function to check if an object inherits a class.


    Args:
        obj: The object to be checked.
        a_class: The class

    Return:
        True or False.
    """
    return isinstance(obj, a_class) and issubclass(obj, a_class)
