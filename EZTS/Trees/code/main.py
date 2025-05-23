from Tree import TreeNode , BinaryTree

from interativePreOrder import PreOrderTraversal

# Create a tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

tree = BinaryTree(root)

print(PreOrderTraversal(tree.root))
