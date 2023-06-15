class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(list1, list2):
    node = list1
    last_node = None
    while node:
        print(node.val)
        node = node.next
        if not node:
            last_node = node

    print(last_node.val)


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)

print(merge(list1=list1, list2=list2))