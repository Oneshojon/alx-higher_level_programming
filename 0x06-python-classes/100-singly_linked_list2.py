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

    @property
    def next_node(self):
        """
        a getter methode to retrieve the pointer to the next Node.

        returns:
	pointer to the next Node.
        """
	return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter: for assigning value to next_node.

        Args:
        value (Node object): A node object or None

        Raises:
        TypeError: If value is neither None nor Node.
        """
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Defines a singly linked list.

    Artributes:
    head: points to the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList.

        Artributs:
        head: points to an empty linked list.
	"""
        self.__head = None
    def sorted_insert(self, value):
        """
        Sorts the Singly Linked list in acsending order.

        Args:
        value (int): value to be inserted into the sorted list.
        """
        new_node = Node(value)
        if self.__head = None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data <\
                    value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    
