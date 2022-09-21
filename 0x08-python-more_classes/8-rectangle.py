#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    Class that defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        An empty class Rectangle that defines a rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """
        Print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            shape = ((str(self.print_symbol) * self.__width) + "\n") * (self.__height)
            return shape[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints a message on deletion
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        dictr = {rect_1: rect_1.area(), rect_2: rect_2.area()}
        if dictr[rect_1] == dictr[rect_2]:
            return rect_1
        else:
            return max(dictr, key=dictr.get)
