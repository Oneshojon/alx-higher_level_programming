#!/usr/bin/python3
"""
Function to append a text to a file.
"""


def append_write(filename="", text=""):
    """
    A function to append text to a file.

    Args:
        filename: Name of the file to append to.
        text: Text to append to the file

    Returns:
        The number of chracters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        written = f.write(text)
    return written
