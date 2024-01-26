from typing import Any


class TreeNode:
    """A class representing a node in a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode with the given value, left child, and right child.

        Parameters:
        - val (int): The value of the node.
        - left (TreeNode): The left child of the node.
        - right (TreeNode): The right child of the node.
        """
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, val: Any):
        self.root = None
        self._initialize(val=val)

    def _initialize(self, val: Any):
        """
        Initialize a binary tree.

        Args:
            val (Any): The value or list of values to initialize the tree with.

        Time Complexity: O(n), where n is the number of values in the input list.
        Space Complexity: O(n), for storing nodes in the tree.
        """
        if isinstance(val, list):
            for value in val:
                self.insert(val=value)
        else:
            self.root = TreeNode(val=val)

    def insert(self, val: int):
        """
        Insert a value into the binary tree.

        Args:
            val (int): The value to be inserted.

        Time Complexity: O(log n) on average for a balanced tree, O(n) in the worst case.
        Space Complexity: O(1) for the iterative version; O(log n) for the recursive version (due to the call stack).
        """
        self.root = self._insert(root=self.root, val=val)

    def _insert(self, root: TreeNode, val: int) -> TreeNode:
        """
        Helper function to recursively insert a value into the binary tree.

        Args:
            root (TreeNode): The root of the current subtree.
            val (int): The value to be inserted.

        Returns:
            TreeNode: The root of the modified subtree.

        Time Complexity: O(log n) on average for a balanced tree, O(n) in the worst case.
        Space Complexity: O(1) for the iterative version; O(log n) for the recursive version (due to the call stack).
        """
        if not root:
            return TreeNode(val=val)
        if val < root.val:
            root.left = self._insert(root=root.left, val=val)
        else:
            root.right = self._insert(root=root.right, val=val)
        return root

    def reverse_tree(self) -> None:
        """
        Reverse the binary tree in place.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        self.root = self._reverse(root=self.root)

    def _reverse(self, root: TreeNode) -> TreeNode:
        """
        Helper function to recursively reverse a binary tree.

        Args:
            root (TreeNode): The root of the current subtree.

        Returns:
            TreeNode: The root of the modified subtree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        if not root:
            return
        aux = root.left
        root.left = root.right
        root.right = aux
        self._reverse(root=root.left)
        self._reverse(root=root.right)
        return root

    def in_order_traversal(self) -> None:
        """
        Perform in-order traversal on the binary tree and print the values.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        self._in_order_traversal(root=self.root)

    def _in_order_traversal(self, root: TreeNode) -> None:
        """
        Helper function to perform in-order traversal on a binary tree and print the values.

        Args:
            root (TreeNode): The root of the current subtree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        if not root:
            return
        self._in_order_traversal(root=root.left)
        print(root.val)
        self._in_order_traversal(root=root.right)

    def pre_order_traversal(self) -> None:
        """
        Perform pre-order traversal on the binary tree and print the values.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        self._pre_order_traversal(root=self.root)

    def _pre_order_traversal(self, root: TreeNode) -> None:
        """
        Helper function to perform pre-order traversal on a binary tree and print the values.

        Args:
            root (TreeNode): The root of the current subtree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        if not root:
            return
        print(root.val)
        self._pre_order_traversal(root=root.right)
        self._pre_order_traversal(root=root.left)

    def post_order_traversal(self) -> None:
        """
        Perform post-order traversal on the binary tree and print the values.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        self._post_order_traversal(root=self.root)

    def _post_order_traversal(self, root: TreeNode) -> None:
        """
        Helper function to perform post-order traversal on a binary tree and print the values.

        Args:
            root (TreeNode): The root of the current subtree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).
        """
        if not root:
            return
        self._post_order_traversal(root=root.right)
        self._post_order_traversal(root=root.left)
        print(root.val)

    def height(self, root: TreeNode):
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
        return max(self.height(root.left), self.height(root.right)) + 1

    def is_balanced(self) -> bool:
        """
        Check if a binary tree is balanced.

        Parameters:
        - root (TreeNode): The root node of the binary tree.

        Returns:
        - bool: True if the binary tree is balanced, False otherwise.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to the call stack).

        Note:
        A binary tree is considered balanced if the heights of the left and right subtrees differ by at most 1. An empty tree is also considered balanced.
        """
        return self._is_balanced(root=self.root)

    def _is_balanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        
        return (
            abs(left - right) <= 1
            and self._is_balanced(root.left)
            and self._is_balanced(root.right)
        )


# Example usage of the BinaryTree class
if __name__ == "__main__":
    values = [3, 9, 20, 15, 7]

    # Create a binary tree
    binary_tree = BinaryTree(val=values)

    # Print the original tree using in-order traversal
    print("Original Tree (In-order Traversal):")
    binary_tree.in_order_traversal()

    # Reverse the binary tree
    binary_tree.reverse_tree()

    # Print the reversed tree using in-order traversal
    print("Reversed Tree (In-order Traversal):")
    binary_tree.in_order_traversal()

    # Perform pre-order traversal on the reversed tree
    print("Reversed Tree (Pre-order Traversal):")
    binary_tree.pre_order_traversal()

    # Perform post-order traversal on the reversed tree
    print("Reversed Tree (Post-order Traversal):")
    binary_tree.post_order_traversal()

    # Check if the tree is balanced
    print(f"Tree is balanced: {binary_tree.is_balanced()}")
