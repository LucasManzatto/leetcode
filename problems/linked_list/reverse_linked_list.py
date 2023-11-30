"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional
from structures.linked_list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        next = None
        while current:
            next = (
                current.next
            )  # stores the next node in the original list before we change the current.next pointer.
            current.next = previous  # reverses the direction of the current node's next pointer, making it point to the previous node.
            previous = current
            current = next
        return previous # previous is the new head of the list (Last element)


root = ListNode(1)
value1 = ListNode(2)
value2 = ListNode(3)
value3 = ListNode(4)
value4 = ListNode(5)
root.next = value1
value1.next = value2
value2.next = value3
value3.next = value4


result = Solution().reverseList(head=root)
while result:
    print(result.val)
    result = result.next

