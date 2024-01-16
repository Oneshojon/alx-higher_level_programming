#!/usr/bin/python3
"""
A base class.
"""
import json


class Base:
    """
    A base class

    Attributes:
        _nb_objects: An object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a new class.

        Args:
            id: A value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that return json string representaion of dictionary.

        Args:
            A dictionary
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
        Method that writes the json string to a file.

        Args:
            list object
        """
    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a jason string to a file

        Args:
            list_obj:
        """
        if list_objs is None:
            list_objs = []
        json_string = cls.\
            to_json_string([b.to_dictionary() for b in list_objs])
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of json string represented by json_string.

        Args:
            json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            new = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file.

        Args:
            cls

        Returns:
           list: List of instances loaded from the file.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_string = f.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_of_dicts]
        except FileNotFoundError:
            return []
