#!/usr/bin/python3
"""
A function that creates an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    A function that creates an object from a JSON file.

    Args:
        filename: The jason file to be converted.

    Returns:
        A Python Object.
    """
    import json
    with open(filename, encoding="utf-8") as content:
        return json.load(content)
