#!/usr/bin/python3
""" this Class form python bytecode for magic objects"""
import math


class MagicClass:
    """the Class constructor"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """does Return the area"""
    def area(self):
        return self.__radius ** 2 * math.pi

    """it Return circumference"""
    def circumference(self):
        return 2 * math.pi * self.__radius
