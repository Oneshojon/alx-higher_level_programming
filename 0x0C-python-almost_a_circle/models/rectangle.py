#!/usr/bin/python3
"""A Rectangle class that inherits from BAse."""


class Rectangle(Base):
    """
    Rectangle class

    Attributes:
        None
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle class.

        Args:
            width (int): Width of rectangle
            height (int): Height of the rectangle
            x (int): x-positio
            y (int): y-position
            id: Id of the element
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter that retrieves the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter method that assigns a value to the width

        Args
            value (int): The value to be assigned.

        Raises: 
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """
        Getter method that retrieves the value of the width
        """
        return self__height

    @height.setter
    def height(self, value):
        """
        Setter That assigns value to height
        """
        validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Retrieves the x value"""
        return self.__x

    @x.setter
    def x(self, value)
