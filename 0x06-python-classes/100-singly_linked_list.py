#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value == None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head == None:
            self.__head = Node(value)
        elif value < self.__head.data:
           self.__head = Node(value, self.__head)
        else:
            __current = self.__head
            while __current.next_node != None and value < __current.next_node.data:
                __current = __current.next_node
            __current.next_node = Node(value)

    def __str__(self):
        __current = self.__head
        strlist = []
        while __current != None:
            strlist.append(__current.data)
            __current = __current.next_node
        return str(strlist)





