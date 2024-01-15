#!/usr/bin/python3
"""A Rectangle class that inherits from BAse."""
from models.base import Base


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
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter That assigns value to height
        """
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Retrieves the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter that assigns value to x
        """
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter that retrieves the value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Method that retrieves the value of y.
        """
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """Method for validating the values"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """Prints the rectangle using #"""
        rec = "\n" * self.y +\
              (" " * self.x + "#" * self.width + "\n") * self.height
        print(rec, end="")

    def __str__(self):
        """Returns the rectanle a in given format."""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Method that update the rectangle class"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Method to update the rectangle class"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns the dictionary representation of
        thr rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
            }
