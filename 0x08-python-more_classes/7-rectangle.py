#!/usr/bin/python3
"""A class to define an empty Rectangle class"""


class Rectangle:
    """
    A class to define an empty rectangle

    Attributes:
        - width (int): The width of the rectangle
        - height (int): The height of the rectangle
    """

    print_symbol = 0
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and  height.

        Args:
            width (int): Width of the rectangle default to 0.
            height (int): Height of the rectangle default to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method that returns the value of the width

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method that sets the value of the width

        Args:
            value (int): An inter value for width

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve height.

        Returns:
            int: The height of the Rectanle class.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method that assigns vallue to height.

        Args:
            value (int): Non negative integer

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public mathod that find area of the rectangle.

        returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public class that return the perimeter of rectangle.

        Returns:
            int: Perimrter of rectangle.
        """
        if self.__width <= 0 or self.__height <= 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: A string representing the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
