#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """
    A class to represent a square

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): The size of the square. Default to zero.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
