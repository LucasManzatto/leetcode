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

from structures.binary_tree import (
    TreeNode,
    reverse_tree,
)
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root=root.left)
        self.invertTree(root=root.right)
        return root


root = TreeNode(val=4)
root.left = TreeNode(val=2)
root.left.left = TreeNode(val=1)
root.left.right = TreeNode(val=3)

root.right = TreeNode(val=7)
root.right.left = TreeNode(val=6)
root.right.right = TreeNode(val=9)

new_root = reverse_tree(root)

# print(Solution().invertTree(root=root))