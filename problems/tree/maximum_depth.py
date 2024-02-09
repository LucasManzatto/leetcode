"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from structures.binary_tree import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


root = TreeNode(val=3)
root.left = TreeNode(val=9)

root.right = TreeNode(val=20)
root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)

solution = Solution().maxDepth(root=root)
print(solution)
