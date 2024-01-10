#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure.
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary with a simple data structure
    for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: Dictionary representation for JSON serialization.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
