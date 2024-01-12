#!/usr/bin/python3
"""
A function to append a text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a text to a file

    Args:
        filename (str): Name of the file to add.
        search_string (str): Str present in th file.
        new_string (str): New string to be added.

    Returns: An appended file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
