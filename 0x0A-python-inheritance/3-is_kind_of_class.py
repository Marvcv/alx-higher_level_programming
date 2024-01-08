#!/bin/python3
"""module containing is_kind_instance method"""
def is_kind_of_class(obj, a_class):
    """Return true if obj is instance of a_class or
    instance of a class that inherited 4rm a_class el false"""
    return isinstance(obj, a_class)
