#!/bin/python3
"""class module BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """raise exception area should b from subclass"""
        raise Exception("area() is not implemented")
