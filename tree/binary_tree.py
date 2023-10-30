import graphviz

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def reverse_tree(root):
    if not root:
        return
    aux = root.left
    root.left = root.right
    root.right = aux
    reverse_tree(root=root.left)
    reverse_tree(root=root.right)
    return root

def in_order_traversal(root: TreeNode):
    if not root:
        return
    in_order_traversal(root.left)
    print(root.val)
    in_order_traversal(root.right)

def pre_order_traversal(root: TreeNode):
    if not root:
        return
    print(root.val)
    pre_order_traversal(root.right)
    pre_order_traversal(root.left)

def post_order_transversal(root: TreeNode):
    if not root:
        return
    post_order_transversal(root.right)
    post_order_transversal(root.left)
    print(root.val)


def visualize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.val))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.val))
            dot.edge(str(node.val), str(node.left.val))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.val))
            dot.edge(str(node.val), str(node.right.val))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')
