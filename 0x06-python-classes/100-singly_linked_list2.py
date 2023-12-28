#!/usr/bin/python3
"""defines a class Node"""


def Node:
    """
    A class to represent a singly linked list..

    Artributes:
    data: conent of the node.
    next_node: Pointer to the next node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
        data (int): value contained in a node.
        next_node: Pointer to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the value

        returns:
        The value retrived
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the value of the Node.

        Arg:
        value (int): an ineger

        Raises:
        TypeError: if values not integer.
        """
	if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
