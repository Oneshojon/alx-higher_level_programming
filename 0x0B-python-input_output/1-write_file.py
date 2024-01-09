#!/usr/bin/python3
"""
FUnction to write into a file.
"""


def write_file(filename="", text=""):
    """
    A function to write to a file.

    Args:
        filename: Name of file to write to.
        text: Text to be written.
    Returns:
        The number of characters read.
    """
    with open(filename, "w", encoding="utf-8") as f:
        written = f.write(text)
    return written
