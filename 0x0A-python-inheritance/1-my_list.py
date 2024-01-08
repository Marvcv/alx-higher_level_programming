#!/bin/python3
"""MyList Module"""
class Mylist(list)
    """my list class inherits from list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
