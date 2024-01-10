#!/usr/bin/python3
"""
A function to write an object in json representation to a file.
"""


def save_to_json_file(my_obj, filename):
    """
    A function to write to a file.

    Args:
        my_obj: The python object.
        filename: Name of the file to write to.

    Returns:
        Nothing.
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
