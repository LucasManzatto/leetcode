"""
Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false


Example 3:
Input: root = []
Output: true
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

from structures.binary_tree import TreeNode
from typing import Optional


class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> bool:
        self.height(root=root)
        return self.max_diameter

    def height(self, root):
        """
        Calculate the height of a binary tree.

        Parameters:
        - root: The root node of the binary tree.

        Returns:
        - The height of the binary tree.

        Example:
        height(root) -> 3

        Note:
        The height of a binary tree is defined as the number of edges in the longest path from the root node to any leaf node. If the tree is empty, the height is 0.
        """
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.max_diameter = max(self.max_diameter, left + right)
        return max(left, right) + 1


root = TreeNode(val=1)
root.left = TreeNode(val=2)

root.right = TreeNode(val=3)
root.right.left = TreeNode(val=4)
root.right.right = TreeNode(val=5)

solution = Solution().diameterOfBinaryTree(root=root)
print(solution)
