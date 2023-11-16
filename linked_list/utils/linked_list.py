class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self, val):
        self.root = ListNode(x=val)

    def append(self, val):
        last = self.root
        while last.next:
            last = last.next
        last.next = ListNode(x=val)

    def push(self, val):
        node = ListNode(x=val)
        node.next = self.root
        self.root = node

    def print(self):
        root = self.root
        while root:
            print(root.val)
            root = root.next
