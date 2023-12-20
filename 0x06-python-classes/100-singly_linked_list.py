#!/usr/bin/python3
"""Defines a class for singly linked list"""


class Node:
    """
    Defines a class for singly linked list

    Artributes:
    __data (int): The data stored in the node
    __next_node (node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
        data (int): The data to be stored in the node.
        next_node (Node, optional): The reference to the next node.
        Defaults to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter to retrieve the data in the node.

        Returns:
        int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter to set the value of the list

        Args:
        value (int): The new data to be stored in the node.

        Raises:
        TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve reference to the next node.

        Returns:
        Node: The reference to the next node.
        """
        return self.__nextnode

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set reference to the next node.

        Args:
        value (Node): The reference to the next node.

        Raises:
        TypeError: if the value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Artributes:
    __head (Node): The head node of the linked list.
    """

    def __init__(self):
        """ Initializes a new instance of the SinglyLinkedList class. """
        self.__head = None  # Private attribute with no getter or setter

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
        list (increasing order).

        Args:
        value (int): The value to be inserted into the list.
        """

        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data <\
                    value:
                current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the entire linked list.

        Returns:
        str: The string representation of the string list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
