#!/usr/bin/python3
""" this is a Class Square that defines a square by
    Private instance attribute: size
    Getter and Setters
    Instantiation with optional size
    size must be an integer
    Public instance method: def area(self)
"""


class Square:
    """itys the Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """its the Size getter"""
    @property
    def size(self):
        return self.__size

    """its the Size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """it returns the current square area"""
    def area(self):
        return self.__size ** 2
