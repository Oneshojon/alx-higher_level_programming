#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    Defines a class for MagicClass

    Arttributes:
    radius (int): radius of a circle
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass.

        Args:
        radius: int radius

        Raises:
        TypeError: radius must be a number
        """
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Finds the area using radius

        Returns: Area
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns circumference based on radius

        Returns: Circumference value
        """
        return 2 * math.pi * self.__radius
