# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """Adds a new node to the beginning of the list"""
        node = DLNode(value)
        first = self.sentinel.next
        first.prev = node
        node.next = first
        node.prev = self.sentinel
        self.sentinel.next = node

    def add_back(self, value: object) -> None:
        """Adds a new node to the end of the list"""
        node = DLNode(value)
        last = self.sentinel.prev
        last.next = node
        node.prev = last
        node.next = self.sentinel
        self.sentinel.prev = node

    def insert_at_index(self, index: int, value: object) -> None:
        """Inserts node at specified index"""
        if index < 0 or index > self.length():
            raise CDLLException
        node = DLNode(value)
        current = self.sentinel
        for i in range(index):
            current = current.next
        next_node = current.next
        next_node.prev = node
        node.next = next_node
        node.prev = current
        current.next = node


    def remove_front(self) -> None:
        """Removes the first node of the list"""
        if self.length() == 0:
            raise CDLLException
        first = self.sentinel.next
        second = first.next
        self.sentinel.next = second
        second.prev = self.sentinel


    def remove_back(self) -> None:
        """Removes the last node from the list"""
        if self.length() == 0:
            raise CDLLException
        last = self.sentinel.prev
        second_last = last.prev
        self.sentinel.prev = second_last
        second_last.next = self.sentinel

    def remove_at_index(self, index: int) -> None:
        """Removes a node a specified index value"""
        if index < 0 or index > self.length() - 1:
            raise CDLLException
        current = self.sentinel
        for i in range(index):
            current = current.next
        next_node = current.next.next
        current.next = next_node
        next_node.prev = current

    def get_front(self) -> object:
        """Returns the value of the first node in the list"""
        if self.length() == 0:
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """Returns the value of the last node in the list"""
        if self.length() == 0:
            raise CDLLException
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """Traverses list and removes first node matching the provided value given"""
        current = self.sentinel
        for i in range(self.length() + 1):
            if current.next.value == value:
                next_node = current.next.next
                current.next = next_node
                next_node.prev = current
                return
            current = current.next


    def count(self, value: object) -> int:
        """Counts the number of elements in the list matching the provided value"""
        current = self.sentinel
        count = 0
        for i in range(self.length() + 1):
            if current.next.value == value:
                count += 1
            current = current.next
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """Swaps two nodes given their indices"""
        if index1 < 0 or index1 > self.length() - 1:
            raise CDLLException
        if index2 < 0 or index2 > self.length() - 1:
            raise CDLLException

        node1 = self.sentinel.next
        for i in range(index1):
            node1 = node1.next  # determines the first node to be swapped
        node1_prev = node1.prev
        node1_next = node1.next

        node2 = self.sentinel.next
        for i in range(index2):
            node2 = node2.next  # determines the second node to be swapped
        node2_prev = node2.prev
        node2_next = node2.next

        if index2 - index1 == 1:  # determines if the nodes are next to each other
            node1_prev.next = node2
            node2.prev = node1_prev
            node2.next = node1

            node1.prev = node2
            node1.next = node2_next
            node2_next.prev = node1
            return

        if index1 - index2 == 1:  # determines if the nodes are next to each other
            node2_prev.next = node1
            node1.prev = node2_prev
            node1.next = node2

            node2.prev = node1
            node2.next = node1_next
            node1_next.prev = node2
            return

        node1_prev.next = node2
        node2.prev = node1_prev
        node2.next = node1_next
        node1_next.prev = node2

        node2_prev.next = node1
        node1.prev = node2_prev
        node1.next = node2_next
        node2_next.prev = node1


    def reverse(self) -> None:
        """Reverses the order of nodes in the list"""

        last = self.sentinel.prev
        first = self.sentinel

        for i in range(self.length() + 1):
            first.next = last
            temp = last.prev
            last.prev = first
            first = first.next
            last = temp

    def sort(self) -> None:
        """"""
        pass

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def remove_duplicates(self) -> None:
        """Deletes all nodes that have duplicate values in a sorted linked list"""
        previous = self.sentinel
        current = self.sentinel.next
        next_curr = current.next

        for i in range(self.length()):
            if current.value == next_curr.value:
                previous.next = next_curr
                next_curr.prev = previous
            previous = previous.next
            current = current.next
            next_curr = next_curr.next

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def add_integer(self, num: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

if __name__ == '__main__':

    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)

    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)

    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))

    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)

    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)

    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))

    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())

    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)

    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    # print('\n# reverse example 1')
    # test_cases = (
    #     [1, 2, 3, 3, 4, 5],
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)

    # print('\n# reverse example 2')
    # lst = CircularList()
    # print(lst)
    # lst.reverse()
    # print(lst)
    # lst.add_back(2)
    # lst.add_back(3)
    # lst.add_front(1)
    # lst.reverse()
    # print(lst)

    # print('\n# reverse example 3')


    # class Student:
    #     def __init__(self, name, age):
    #         self.name, self.age = name, age
    #
    #     def __eq__(self, other):
    #         return self.age == other.age
    #
    #     def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)


    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)
    #
    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)

    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)

    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)

    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)

    # print('\n# odd_even example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], list('ABCDE'),
    #     [], [100], [100, 200], [100, 200, 300],
    #     [100, 200, 300, 400],
    #     [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)

    # print('\n# add_integer example 1')
    # test_cases = (
    #   ([1, 2, 3], 10456),
    #   ([], 25),
    #   ([2, 0, 9, 0, 7], 108),
    #    ([9, 9, 9], 9_999_999),
    #)
    # for list_content, integer in test_cases:
    #    lst = CircularList(list_content)
    # print('INPUT :', lst, 'INTEGER', integer)
    # lst.add_integer(integer)
    # print('OUTPUT:', lst)
