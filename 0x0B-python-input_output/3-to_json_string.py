#!/usr/bin/python3
"""
FUnction That returns a JSON representation of an object
"""


def to_json_string(my_obj):
    """
    A function to return JSON representation of an object

    Args:
        my_obj: The object to be converted.

    Returns:
        JASON version of obj.
    """
    import json
    return json.dumps(my_obj)
