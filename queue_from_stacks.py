# Course: CS261 - Data Structures
# Student Name: Jordan Hendricks
# Assignment: Assignment 3
# Description: Implementation of Stack ADT using Linked List


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # ------------------------------------------------------------------ #

    def enqueue(self, value: object) -> None:
        """Adds a new value to the end of the que"""
        return self.s1.push(value)

    def dequeue(self) -> object:
        """Removes and returns the value at the end of the que"""
        if self.s1.is_empty() is True:
            raise QueueException

        for i in range(self.s1.size()):
            value = self.s1.pop()
            self.s2.push(value)

        ret_val = self.s2.pop()
        for i in range(self.s2.size()):
            value2 = self.s2.pop()
            self.s1.push(value2)
        return ret_val

        # return self.s1.pop()

# BASIC TESTING
# if __name__ == "__main__":
#     pass
#
#     print('\n# enqueue example 1')
#     q = Queue()
#     print(q)
#     for value in [1, 2, 3, 4, 5]:
#         q.enqueue(value)
#     print(q)
#
#     print('\n# dequeue example 1')
#     q = Queue()
#     for value in [1, 2, 3, 4, 5]:
#         q.enqueue(value)
#     print(q)
#     for i in range(6):
#         try:
#             print(q.dequeue(), q)
#         except Exception as e:
#             print("No elements in queue", type(e))
#


