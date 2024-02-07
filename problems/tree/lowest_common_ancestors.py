"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node <= 109
All Node are unique.
p != q
p and q will exist in the BST.
"""

from utils.binary_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or root.val in (p.val, q.val):
            return root
        result_left = self.lowestCommonAncestor(root=root.left, p=p, q=q)
        result_right = self.lowestCommonAncestor(root=root.right, p=p, q=q)
        if result_left and result_right:
            return root
        return result_left or result_right


root = TreeNode(val=6)
root.left = TreeNode(val=2)
root.right = TreeNode(val=8)

root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=4)

root.right.left = TreeNode(val=7)
root.right.right = TreeNode(val=9)

root.left.right.left = TreeNode(val=3)
root.left.right.right = TreeNode(val=5)


# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)

p = TreeNode(val=3)
q = TreeNode(val=5)
print(Solution().lowestCommonAncestor(root=root, p=p, q=q).val)
