#!/usr/bin/python3
"""Class to prevent dynamic new instance artribute"""

class LockedClass:
    __slots__ = ('first_name',)

    def __init__(self):
        pass
