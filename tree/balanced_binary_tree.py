"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from utils.binary_tree import (
    TreeNode,
    reverse_tree,
)
from typing import Optional
import math


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.balanced(root=root)

    def balanced(
        self,
        root: Optional[TreeNode],
        max_diff: int = 0,
        total_right: int = 0,
        total_left: int = 0,
    ) -> Optional[TreeNode]:
        if not root:
            return 1
        total_right = self.balanced(
            root=root.right, max_diff=max_diff, total_right=total_right + 1
        )
        # print(root.val, total_right)
        total_left = self.balanced(
            root=root.left, max_diff=max_diff, total_left=total_left + 1
        )
        print(root.val, total_left)
        max_diff = max(max_diff, abs(total_left - total_right))
        return max_diff < 1


root = TreeNode(val=3)
root.left = TreeNode(val=9)
root.right = TreeNode(val=20)

root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)


root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.right = TreeNode(val=2)

root.left.left = TreeNode(val=3)
root.left.right = TreeNode(val=3)

root.left.left.left = TreeNode(val=4)
root.left.left.right = TreeNode(val=4)

print(Solution().isBalanced(root=root))

matrix = [[1,2,3], [4,5,6]]

zero_matrix = [[0 for _ in row] for row in matrix]

print(matrix)
print(new_matrix)