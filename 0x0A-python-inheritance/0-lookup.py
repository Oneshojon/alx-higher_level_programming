#!/usr/bin/python3
"""
A function to look up all the Artributes of an Object

Attributes:
lookup: rturns a list.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Object to inspect.

    Returns:
        list: List of Arttributes and method names.
    """
    return dir(obj)
