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
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            json_string = cls.\
                to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of json string represented by json_string.

        Args:
            json_string
        """
        if json_string is None or json_string == []:
            return []
        return json_string

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width. o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open("{}.csv".format(cls.__name__), 'w', newline='',
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)
