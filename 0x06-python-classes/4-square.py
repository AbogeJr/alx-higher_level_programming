#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class Square that defines a square'''
    def __init__(self, size=0):
        '''The size of a square is crucial for a square, many things depend \
        of it (area computation, etc.). It is important to keep to keep \
        this value private so as to ensure the class builder controls \
        the type and value of this attribute'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Public instance method that r
eturns te current square area'''
        return self.__size ** 2

    @property
    def size(self):
        '''Retrieve private instance attribute size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Property setter to change the value of size'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
