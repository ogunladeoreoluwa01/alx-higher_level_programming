#!/usr/bin/python3
"""In this module, we would see an introduction to linked lists in python
for the first time"""


class Node:
    """This class contains a python representation of a node
        an init, a size, and area, then getter and setter"""
    def __init__(self, data, next_node=None):
        """This initializes the Node a safe mode"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """This is a getter function.
            It returns the value of data safely"""
        return (self.__data)

    @data.setter
    def data(self, data):
        """This is the setter function. It prevents unwarranted modification
        of the data attribute by users"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This node holds the next of the linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This sets the next node safely without
        an unwarranted change of value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This is a python implementation of the linked
    list that gave me so much trouble in C"""
    def __init__(self):
        """This intializes the list with a private
        no protected member name head. This is the
        head of the linked list"""
        self.head = None

    def sorted_insert(self, value):
        """This unique function creates and appends to the linked list
        it then sorts it to make sure the nodes are in ascending order"""
        newnode = Node(value)
        if self.head:
            curr = self.head
            if curr.data >= newnode.data:
                newnode.next_node = curr
                self.head = newnode
            else:
                while curr.next_node is not None:
                    if curr.next_node.data >= newnode.data:
                        temp = curr.next_node
                        newnode.next_node = temp
                        break
                    curr = curr.next_node
                curr.next_node = newnode
        else:
            self.head = newnode

    def __str__(self):
        """This allows the list to be printed or viewed, not a a class
        as it is, but line a linear arrangement, showing its nodes"""
        result = ""
        if not self.head:
            return result
        current = self.head
        while current.next_node:
            result += str(current.data) + "\n"
            current = current.next_node
        result += str(current.data)
        return result
