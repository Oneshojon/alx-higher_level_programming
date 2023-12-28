#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """
    A class that defines a quare.

    Artributes:
    size (int): The size of the square.
    position (tuple): determines the geometric position of the square.
    """
    @property
    def size(self):
    """
    To retireve the size of the square.

    Returns:
    The size of the square.
    """
    return self.__size

    @setter.__size
    def size(self, value):
    """
    Setter that aets the value of size.

    Artribute:
    value (int): The value to be set.
    
    Raise:
    TypeError: If value is not of type int
    ValueError: if value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value

    @property
    def position(self):
        """
        To retieve the position of the square.

        Returns: The position.
        """
	return self.__position
