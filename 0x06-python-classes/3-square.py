#!/usr/bin/python3
""" Heere is the Class Square that defines a square by
    Private instance attribute: size
    Instantiation with optional size
    size must be an integer
"""


class Square:
    """this is the Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """this returns the current square area"""
    def area(self):
        return self.__size * self.__size
