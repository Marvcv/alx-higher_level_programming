#!/usr/bin/python3
"""Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """returns true if obj is instance of a class inh
    directly /indirectly otherwise false"""
    return isinstance(obj, a_class) and type(obj) != a_class
