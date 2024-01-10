#!/usr/bin/python3
"""Class that defines students."""


class Student:
    """
    Creates a Student class.

    Attributes:
        to_json: Retireves dictionary representation of Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student class.

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): Student Age

        Return: A New instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method to retrieve dictionary representation of student instance.

        Args:
            None

        Returns: Nothing
        """
        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                json_dict[key] = value
        return json_dict
