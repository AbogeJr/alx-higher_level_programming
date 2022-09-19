#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    Class that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        An empty class Rectangle that defines a rectangle
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            shape = (("#" * self.__width) + "\n") * (self.__height)
            return shape[:-1]

    @property
    def width(self):
        """
        Property getter to retrieve value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter to set value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property getter to retrieve value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter to set value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
