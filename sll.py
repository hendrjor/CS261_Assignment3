# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """Adds a new node at the beginning of the list"""
        new_node = SLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """Adds a node to the back of the list"""
        new_node = SLNode(value)
        current = self.head
        self.add_back_helper(new_node, current)

    def add_back_helper(self, new_node, current):
        """Helper function keeps track of current node"""
        if current.next == self.tail:
            current.next = new_node
            new_node.next = self.tail
            return
        current = current.next
        self.add_back_helper(new_node, current)

    def insert_helper(self, count, index, current, new_node):
        """Helper function to keep track of current node and value"""
        if count == index:
            after = current.next
            current.next = new_node
            new_node.next = after
            return
        current = current.next
        count += 1
        self.insert_helper(count, index, current, new_node)

    def insert_at_index(self, index: int, value: object) -> None:
        """Inserts a value at an index in the linked list"""
        if index < 0 or index > self.length():
            raise SLLException
        new_node = SLNode(value)
        count = 0
        current = self.head
        self.insert_helper(count, index, current, new_node)

    def remove_front(self) -> None:
        """Removes the first node from the list"""
        if self.length() <= 0:
            raise SLLException

        self.head.next = self.head.next.next

    def remove_back(self) -> None:
        """Removes the last node from the list"""
        if self.length() <= 0:
            raise SLLException

        current = self.head
        self.remove_back_helper(current)

    def remove_back_helper(self, current):
        """Helps go through the list to remove the last node"""
        if current.next.next == self.tail:
            current.next = self.tail
            return
        current = current.next
        self.remove_back_helper(current)

    def remove_at_index(self, index: int) -> None:
        """Removes a node at an index"""
        if index < 0 or index > self.length() - 1:
            raise SLLException
        count = 0
        current = self.head
        self.remove_index_helper(count, index, current)

    def remove_index_helper(self, count, index, current):
        """Helps keep track of node and removes a node at desired index"""
        if count == index:
            current.next = current.next.next
            return
        current = current.next
        count += 1
        self.remove_index_helper(count, index, current)


    def get_front(self) -> object:
        """Returns the value from the first node in the list"""
        if self.length() <= 0:
            raise SLLException
        node = self.head.next
        return node.value

    def get_back(self) -> object:
        """Returns the value from the last node in the list"""
        if self.length() <= 0:
            raise SLLException
        current = self.head
        return self.get_back_helper(current)

    def get_back_helper(self, current):
        """Helps keep track of node and removes last node"""
        if current.next == self.tail:
            return current.value
        current = current.next
        return self.get_back_helper(current)

    def remove(self, value: object) -> bool:
        """Removes the first node in the list that matches the 'value' given"""
        current = self.head
        return self.remove_helper(current, value)

    def remove_helper(self, current, value):
        """Parses through list until a node with the correct value is found or the end of the list is reached"""
        if current.next.value == value:
            current.next = current.next.next
            return True
        elif current.next == self.tail:
            return False
        current = current.next
        return self.remove_helper(current, value)

    def count(self, value: object) -> int:
        """Counts the number of elements in the list that match the provided 'value'"""
        current = self.head
        count = 0
        return self.count_helper(current, value, count)

    def count_helper(self, current, value, count):
        """Parses through list until a node with the correct value is found or the end of the list is reached"""
        if current.next.value == value:
            count += 1
        elif current.next == self.tail:
            return count
        current = current.next
        return self.count_helper(current, value, count)

    def slice(self, start_index: int, size: int) -> object:
        """Returns a new LinkedList containing nodes from the start index based on the length given"""
        if start_index < 0 or start_index > self.length() - 1:
            raise SLLException
        elif start_index + size > self.length() or size < 0:
            raise SLLException
        new_list = LinkedList()
        end_index = start_index + size - 1
        current = self.head
        current_index = 0
        return self.slice_helper(current, current_index, start_index, end_index, new_list)

    def slice_helper(self, current, current_index, start_index, end_index, new_list):
        """Parses through each node to determine the new LinkedList's contents """
        if start_index <= current_index <= end_index:
            new_list.add_back(current.next.value)
        if current.next == self.tail:
            return new_list
        current_index += 1
        current = current.next
        return self.slice_helper(current, current_index, start_index, end_index, new_list)

# if __name__ == '__main__':

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)

    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)

    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))


    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))


    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)


    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)


    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))


    # print('\n# get_back example 1')
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())


    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)


    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")


    # print('\n# slice example 2')
    # list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")
