#!/usr/bin/python3
"""Square class based on Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class for Square

    Agguments:
        width:
        heieght:
        x:
        y:
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialiaes a square.

        Args:
            size (int) Size of the square.
            x (int): X-coordinates.
            y (int): Y-coordinate
            id (int): Identifier.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Method that displays the returns the triangle as a string.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter that retrieves the value of width.

        Returns:
            The value of width.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Method that assign a value to width.

        Args:
            Value: Value to be assigned.
        """
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """
        A method to update the class

        Args:
            args: method
            kwargs: another
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """
        Updates the square class

        Args:
            args:
            kwargs:
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """
        Method that returns a dictionary representation or the class
        attributes

        Arg:
            None
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
            }
