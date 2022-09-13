#!/usr/bin/python3
"""Define the class Node"""


class Node:
    """Represents a Node in a singly linked list
    Attributes:
        __data (int): data stored inside the Node
        __next_node (node): next node in the linked list
    """
    def __init__(self, data, next_node=None):
        """Initializing the node
        Args:
           data (int): data stored inside the Node
           next_node (node): next node in the linked list
        Returns:
            None
        """
        self.data = data
        self.next_node = next_node
    """Property the Getter"""
    @property
    def data(self):
        """Getter of __data
        Returns:
            data stored inside the Node
        """
        return self.__data
    """Setter"""
    @data.setter
    def data(self, value):
        """setter of __data
        Args:
            data (int): data stored inside the node
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    """Property"""
    @property
    def next_node(self):
        """Getter of __next_node
        Returns:
            The next node in the linked list
        """
        return self.__next_node
    """Setter"""
    @next_node.setter
    def next_node(self, value):
        """setter of __next_data
        Args:
            next_node (node): next node in the linked list
        Returns:
            None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    """String node"""
    def __str__(self):
        """String representing the Node instance
        Returns:
            Format string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """Represents a singly linked list
    Attributes:
        __head (Node): head of the linked list
    """
    def __init__(self):
        """Initializing the linked list
        Returns:
            None
        """
        self.__head = None
    """Sort out the insert"""
    def sorted_insert(self, value):
        """Insert a new Node instance into the correct sorted position
        Args:
           values (int): data stored inside the new node
        Returns:
            None
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
    """String representing the singly"""
    def __str__(self):
        """String representing the singly linked list
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
