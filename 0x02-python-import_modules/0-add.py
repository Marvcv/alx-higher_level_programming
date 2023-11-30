#!/usr/bin/python3

"""
This script demonstrates the usage of an 'add' function imported from the 'add_0' module.
It performs addition of two numbers and prints the result.
"""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))

