#!/usr/bin/python3
"""Creates a square class"""


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

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
        int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
        value (int): The new size of the square.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of a square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints to the stdout square with #

        prints an empty line if the size is zero
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
