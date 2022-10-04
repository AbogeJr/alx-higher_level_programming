#!/usr/bin/python3
"""
This module implements a Rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def __width(self):
        """width getter"""
        return self.__width

    @__width.setter
    def __width(self, width):
        """width setter"""
        self.__width = width

    @property
    def __height(self):
        """height getter"""
        return self.__height

    @__height.setter
    def __height(self, height):
        """height setter"""
        self.__height = height

    @property
    def __x(self):
        """x getter"""
        return self.__x

    @__x.setter
    def __x(self, x):
        """x setter"""
        self.__x = x

    @property
    def __y(self):
        """y getter"""
        return self.__y

    @__y.setter
    def __y(self, y):
        """y setter"""
        self.__y = y
