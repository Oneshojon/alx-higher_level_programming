#!/usr/bin/python3
"""A class to inherit the class 'list'"""


class MyList(list):
    """
    Class to inherit attributes from list.

    Attributes:
        print_sorted: print a list

    Args:
        list: A list of integers.
    """
    def print_sorted(self):
        """
        public method to print list in ascending order.

        args:
            None
        """
        list1 = self[:]
	list1.sor()
	print(list1)
