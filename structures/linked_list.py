from typing import Any, Iterator


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
    """

    def __init__(self, val: Any | list):
        """
        Initialize a new singly linked list.

        Args:
            val (Union[Any, list]): The initial value of the linked list.
        """
        if isinstance(val, list):
            self.root = ListNode(x=val[0])
            self.append(val=val[1:])
        else:
            self.root = ListNode(x=val)

    def append(self, val: Any | list):
        """
        Append a value or a list of values to the end of the linked list.

        Args:
            val (Union[Any, list]): The value or list of values to be appended.
        """
        last = self.last_node()
        if isinstance(val, list):
            self._append_list(node=last, values=val)
        else:
            last.next = ListNode(x=val)

    def _append_list(self, node: ListNode, values: list[Any]):
        """
        Append a list of values to the end of the linked list.

        Args:
            node (ListNode): The current last node in the linked list.
            values (list[Any]): The list of values to be appended.
        """
        for x in values:
            node.next = ListNode(x=x)
            node = node.next

    def push(self, val: Any):
        """
        Prepend a value to the front of the linked list.

        Args:
            val (Any): The value to be prepended.
        """
        node = ListNode(x=val)
        node.next = self.root
        self.root = node

    def last_node(self) -> ListNode:
        """
        Get the last node of the linked list.

        Returns:
            ListNode: The last node of the linked list.
        """
        last = self.root
        while last.next:
            last = last.next
        return last

    def has_cycle(self) -> bool:
        """
        Checks if the linked list contains a cycle using Floyd's Tortoise and Hare algorithm.

        Returns:
            bool: True if a cycle is present, False otherwise.
        """
        first_pointer = self.head
        second_pointer = self.head
        while second_pointer and second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
            if first_pointer == second_pointer:
                return True
        return False

    def reversed_list(self) -> ListNode:
        """
        Reverses the direction of the linked list.

        Returns:
            ListNode: The new head of the reversed linked list (previously the last element).
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
        """
        self.root = self.reversed_list()

    def size(self) -> int:
        """
        Return the number of nodes in the linked list.

        Returns:
            int: The number of nodes in the linked list.
        """
        node = self.root
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def to_string(self) -> str:
        """
        Convert the linked list to a string.

        Returns:
            str: A string representation of the linked list.
        """
        list = []
        root = self.root
        while root:
            list.append(root.val)
            root = root.next
        return str(list)

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
