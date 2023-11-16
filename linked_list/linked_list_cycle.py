"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional
from utils.linked_list import ListNode, SinglyLinkedList


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first_pointer = head
        second_pointer = head
        while second_pointer and second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
            if first_pointer == second_pointer:
                return True
        return False


value1 = ListNode(2)
value2 = ListNode(0)
value3 = ListNode(-4)
root = ListNode(1)
root.next = value1
value1.next = root
# value2.next = value3
# value3.next = value1

pointer1 = 0
pointer2 = 0


# list = SinglyLinkedList(val=3)
# list.append(val=2)
# list.append(val=0)
# list.append(val=-4)

result = Solution().hasCycle(head=root)
print(result)
