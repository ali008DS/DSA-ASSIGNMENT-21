class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []

    node_map = {}  # To store the last node at each horizontal distance
    queue = [(root, 0)]

    while queue:
        node, hd = queue.pop(0)
        node_map[hd] = node.val

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the node_map by horizontal distance and extract the values
    bottom_nodes = [node_map[hd] for hd in sorted(node_map)]

    return bottom_nodes

# Examples:
# Constructing the binary tree for the first example
root1 = TreeNode(20)
root1.left = TreeNode(8)
root1.right = TreeNode(22)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(25)
root1.left.right.left = TreeNode(10)
root1.left.right.right = TreeNode(14)
print(bottom_view(root1))  # Output: [5, 10, 3, 14, 25]

# Constructing the binary tree for the second example
root2 = TreeNode(20)
root2.left = TreeNode(8)
root2.right = TreeNode(22)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(25)
root2.left.right.left = TreeNode(10)
root2.left.right.right = TreeNode(14)
print(bottom_view(root2))  # Output: [5, 10, 4, 14, 25]
