from typing import Any


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
            for x in val:
                last.next = ListNode(x=x)
                last = last.next
        else:
            last.next = ListNode(x=val)

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

    def __repr__(self):
        return "SinglyLinkedList()"

    def __str__(self):
        list = []
        root = self.root
        while root:
            list.append(root.val)
            root = root.next
        return str(list)
