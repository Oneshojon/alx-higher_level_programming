#!/usr/bin/python3
"""Function to check if an object inherits from class.

Attribute:
is_same_class: returns True or False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.


    Args:
        obj: The object to be checked.
        a_class: The class

    Return:
        True or False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
