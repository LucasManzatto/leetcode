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
import os, sys

path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0] + "\\"
sys.path.append(path)

from typing import Optional
from structures.linked_list import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


root = ListNode(1)
value1 = ListNode(2)
value2 = ListNode(3)
value3 = ListNode(4)
value4 = ListNode(5)
value5 = ListNode(6)
root.next = value1
value1.next = value2
value2.next = value3
value3.next = value4
value4.next = value5


result = Solution().middleNode(head=root)
while result:
    print(result.val)
    result = result.next
