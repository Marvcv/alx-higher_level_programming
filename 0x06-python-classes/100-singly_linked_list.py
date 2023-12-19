#!/usr/bin/python3
"""FOR This module contains a class that defines a square.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
"""


class Node():
    """THIS IS THE Node Class."""

    def __init__(self, data, next_node=None):
        """Initialization of Node Class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """THE Data"""
        return self.__data

    @data.setter
    def data(self, DataValue):
        """THE Set data"""
        if type(DataValue) != int:
            raise TypeError("data must be an integer")
        self.__data = DataValue

    @property
    def next_node(self):
        """THE Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, NodeValue):
        """THE set Node"""
        if NodeValue is not None and not isinstance(NodeValue, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = NodeValue


class SinglyLinkedList():
    """THE Class SinglyLinkedList"""
    def __init__(self):
        """Initialization of SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, DataValue):
        """THE Inserts a nodes"""
        NewNode = Node(DataValue)
        if self.__head is None:
            self.__head = NewNode
            return
        if DataValue < self.__head.data:
            NewNode.next_node = self.__head
            self.__head = NewNode
            return
        actual = self.__head
        while DataValue >= actual.data:
            prev = actual
            if actual.next_node:
                actual = actual.next_node
            else:
                actual.next_node = NewNode
                return
        prev.next_node = NewNode
        NewNode.next_node = actual

    def __str__(self):
        """Class As a String"""
        strg = ""
        actual = self.__head
        while actual:
            strg += str(actual.data) + "\n"
            actual = actual.next_node
        return strg[:-1]
