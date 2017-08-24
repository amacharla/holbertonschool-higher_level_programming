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
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            __current = self.__head
            while __current.next_node is not None:
                if value < __current.next_node.data:
                    break
                __current = __current.next_node
            __current.next_node = Node(value, __current.next_node)

    def __str__(self):
        __current = self.__head
        strlist = []
        while __current is not None:
            strlist.append(str(__current.data))
            __current = __current.next_node
        return '\n'.join(strlist)
