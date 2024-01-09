#!/usr/bin/python3
"""Module containing is_samee_class method"""
def is_same_class(obj, a_class):
    """return:
    True: If object is exactly an instance of specified class
    False: otherwise"""
    return type(obj)== a_class
