#!/usr/bin/python3
"""
Function to read a file
"""


def read_file(filename=""):
    """
    A function that reads a text file and prints it to stdout

    Args:
        filename: The name of file to read.

    Returns:
        Nothing
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
