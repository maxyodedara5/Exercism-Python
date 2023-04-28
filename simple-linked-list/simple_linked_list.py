"""Simple linked list in style of stack"""

from typing import Any


class Node:
    """Node for linked list"""
    def __init__(self, value):
        self.value_item = value
        self.next_node_address = None
        self.is_head = False

    def value(self):
        """Value of node"""
        return self.value_item

    def next(self):
        """Address of next node"""
        return self.next_node_address


class LinkedList:
    """Simple linked list in style of stack"""
    def __init__(self, values: Any = []) -> None:
        self.length = len(values)

        if len(values) > 1:
            self.head_node = Node(values[-1])
            self.head_node.is_head = True
            last_node = self.head_node
            for value in values[:-1][::-1]:
                new_node = Node(value)
                last_node.next_node_address = new_node
                last_node = new_node

        if len(values) == 1:
            self.head_node = Node(values[0])
            self.head_node.is_head = True

        if len(values) == 0:
            self.head_node = None

        # Variables for iteration guards
        self.current_node = self.head_node
        self.iteration_counter = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration_counter == self.length:
            raise StopIteration

        current_value = self.current_node.value()
        self.current_node = self.current_node.next_node_address
        self.iteration_counter += 1
        return current_value

    def head(self):
        """Returns the value of top of linked list"""
        if self.length == 0:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        """Inserts the value of top of linked list"""
        self.length += 1
        if self.length == 1:
            self.head_node = Node(value)
            self.head_node.is_head = True
            return

        new_head = Node(value)
        new_head.is_head = True
        self.head_node.is_head = False
        new_head.next_node_address = self.head_node
        self.head_node = new_head
        return

    def pop(self):
        """Removes the value of top of linked list"""
        if self.length == 0:
            raise EmptyListException("The list is empty.")

        self.length -= 1
        value_of_pop = self.head_node.value()
        headless_node = self.head_node.next_node_address

        if headless_node is not None:
            headless_node.is_head = True
        self.head_node = headless_node

        return value_of_pop


    def reversed(self):
        """Provides a reversed list of all values in linked list"""
        if self.length < 2:
            if self.length == 0:
                return []

            if self.length == 1:
                return [self.head_node.value()]

        values = []
        current_node = self.head_node
        while current_node.next() is not None:
            values.append(current_node.value())
            current_node = current_node.next_node_address

        values.append(current_node.value())
        return values[::-1]

class EmptyListException(Exception):
    """Class for raising empty exception"""
