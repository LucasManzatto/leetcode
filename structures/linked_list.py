from typing import Any, Iterator
from collections.abc import Iterable
import inspect


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        root (ListNode): The root node of the linked list.
        tail (ListNode): The tail node of the linked list.

    Methods:
        __init__(self, val: Any | list): Initialize a new singly linked list.
        append(self, val: Any): Append a value to the end of the linked list.
        extend(self, values: list): Extend the linked list with a list of values.
        push(self, val: Any): Prepend a value to the front of the linked list.
        last_node(self) -> ListNode: Get the last node of the linked list.
        middle_node(self) -> ListNode: Get the middle node of the linked list.
        has_cycle(self) -> bool: Checks if the linked list contains a cycle.
        reverse(self): Reverse the order of nodes in the linked list.
        size(self) -> int: Return the number of nodes in the linked list.
        to_string(self) -> str: Convert the linked list to a string.
        __repr__(self) -> str: Return a string representation of the linked list for debugging.
        __str__(self) -> str: Return a string representation of the linked list.
        __reversed__(self) -> Iterator[Any]: Return a reverse iterator for the linked list.
        __len__(self) -> int: Get the length of the linked list.
        __iter__(self, other) -> Iterator[Any]: Returns an iterator object.
    """

    def __init__(self, val: Any | list):
        """
        Initialize a new singly linked list.

        Args:
            val (Union[Any, list]): The initial value of the linked list.
        """
        if val is None:
            raise ValueError("Input value cannot be None.")
        is_iterable = isinstance(val, Iterable)
        self.counter = 1
        if is_iterable:
            self.root = ListNode(x=val[0])
            self.tail = self.root
            self.extend(values=val[1:])
        else:
            self.root = ListNode(x=val)
            self.tail = self.root

    def append(self, val: Any):
        """
        Append a value to the end of the linked list.

        Args:
            val (Any): The value to be appended.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if val is None:
            raise ValueError("Input value cannot be None.")
        last = self.tail
        last.next = ListNode(x=val)
        self.tail = last.next
        self.counter += 1

    def extend(self, values: list):
        """
        Extend the linked list with a list of values.

        Args:
            values (list): The list of values to be appended.

        Time Complexity: O(n), where n is the length of the input list.
        Space Complexity: O(1)
        """
        is_iterable = isinstance(values, Iterable)
        if not is_iterable:
            raise ValueError("Input value must be iterable.")
        last = self.tail
        for x in values:
            self.append(val=x)

    def push(self, val: Any):
        """
        Prepend a value to the front of the linked list.

        Args:
            val (Any): The value to be prepended.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if val is None:
            raise ValueError("Input value cannot be None.")
        node = ListNode(x=val)
        node.next = self.root
        self.root = node
        self.counter += 1
        return node

    def last_node(self) -> ListNode:
        """
        Get the last node of the linked list.

        Returns:
            ListNode: The last node of the linked list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.tail

    def middle_node(self) -> ListNode:
        """
        Get the middle node of the linked list.

        Returns:
            ListNode: The middle node of the linked list.

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1)
        """
        if self.has_cycle():
            raise ValueError("Linked list contains a cycle.")
        slow = self.root
        fast = self.root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_cycle(self) -> bool:
        """
        Checks if the linked list contains a cycle using Floyd's Tortoise and Hare algorithm.

        Returns:
            bool: True if a cycle is present, False otherwise.

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1)
        """
        first_pointer = self.root
        second_pointer = self.root
        while second_pointer and second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
            if first_pointer == second_pointer:
                return True
        return False

    def _reversed_list(self) -> ListNode:
        """
        Reverses the direction of the linked list.

        Returns:
            ListNode: The new head of the reversed linked list (previously the last element).

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1)
        """
        current = self.root
        previous = None
        next = None
        while current:
            next = (
                current.next
            )  # stores the next node in the original list before we change the current.next pointer.
            current.next = previous  # reverses the direction of the current node's next pointer, making it point to the previous node.
            previous = current
            current = next
        return previous  # previous is the new head of the list (Last element)

    def reverse(self):
        """
        Reverse the order of nodes in the linked list.

        This method modifies the linked list in place by reversing the order of its nodes.
        The head of the original list becomes the new tail, and the last node becomes the new head.

        Example:
        ```
        linked_list = LinkedList([1, 2, 3, 4, 5])
        linked_list.reverse_list()
        print(linked_list)  # Output: 5 -> 4 -> 3 -> 2 -> 1
        ```

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1)
        """
        self.root = self._reversed_list()

    def size(self) -> int:
        """
        Return the number of nodes in the linked list.

        Returns:
            int: The number of nodes in the linked list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.counter

    def _equals(self, other) -> bool:
        if not type(self) == type(other):
            raise ValueError("Input value must be a SinglyLinkedList")
        current, current_other = self.root, other.root
        if len(self) != len(other):
            return False

        while current and current_other:
            if current.val != current_other.val:
                return False
            current = current.next
            current_other = current_other.next
        return True

    def to_string(self) -> str:
        """
        Convert the linked list to a string.

        Returns:
            str: A string representation of the linked list.

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(n)
        """
        list = []
        root = self.root
        while root:
            list.append(root.val)
            root = root.next
        return str(list)

    def __eq__(self, other) -> bool:
        return self._equals(other=other)

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list for debugging.

        Returns:
            str: A string representation of the linked list.
        """
        return "SinglyLinkedList()"

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        return self.to_string()

    def __reversed__(self) -> Iterator[Any]:
        """
        Return a reverse iterator for the linked list.

        Yields:
            Any: Values of the linked list in reverse order.
        """
        current = self.reversed_list()
        while current:
            yield current.val
            current = current.next

    def __len__(self) -> int:
        """
        Get the length of the linked list.

        Returns:
            int: The number of nodes in the linked list.
        """
        return self.size()

    def __iter__(self):
        """
        Returns an iterator object that allows iteration over the values of the linked list.

        Yields:
            The value of each node in the linked list.

        Example:
            linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
            for value in linked_list:
                print(value)
            Output:
                1
                2
                3
                4
                5
        """
        current = self.root
        while current:
            yield current.val
            current = current.next


if __name__ == "__main__":
    linked_list = SinglyLinkedList([1, 2, 3])  # Initialize a linked list with values
    other_linked_list = SinglyLinkedList(
        [1, 2, 3]
    )  # Initialize a linked list with values
    is_equal = linked_list == other_linked_list  # Check if two lists are equal
    linked_list.append(4)  # Append a value to the end of the list
    linked_list.extend([5, 6, 7])  # Extend the list with a list of values
    linked_list.push(0)  # Prepend a value to the front of the list
    last_node = linked_list.last_node()  # Get the last node of the list
    middle_node = linked_list.middle_node()  # Get the middle node of the list
    has_cycle = linked_list.has_cycle()  # Check if the list contains a cycle
    linked_list.reverse()  # Reverse the order of nodes in the list
    size = linked_list.size()  # Get the number of nodes in the list
    string_representation = linked_list.to_string()  # Convert the list to a string
    print(linked_list)
