#!/usr/bin/python3
"""
A function that returns an objectrepresented in python string.
"""


def from_json_string(my_str):
    """
    Changes json to python object.

    Args:
        my_str: The json string

    Returns:
        A python object.
    """
    import json
    return json.loads(my_str)
