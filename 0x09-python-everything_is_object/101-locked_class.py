#!/usr/bin/python3
"""Class to prevent dynamic new instance artribute"""


class LockedClass:
    """
    Locked classs that prevent instanciation

    Args:
        None
    """
    __slots__ = ('first_name',)

    def __init__(self):
        """
        initializess nothing

        Returns:
        Nothing
        """
        pass
