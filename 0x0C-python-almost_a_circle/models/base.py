#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
"""


class Base:
    """
    This class will be the “base” of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
