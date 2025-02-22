# TODO: Inorder Traversal.. LEFT -> ROOT -> RIGHT
# Time Complexity: O(n)
# Space Complexity: O(n)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if self.val:
            if key < self.val:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                    self.left.insert(key)
            elif key > self.val:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        else:
            self.val = key


def inOrderTraversal(root, level=0, prefix="Root: "):
    if root:
        inOrderTraversal(root.left, level + 1, "L--- ")
        print(" " * (level * 4) + prefix + str(root.val))
        inOrderTraversal(root.right, level + 1, "R--- ")

# Example usage
root = TreeNode(50)
root.insert(30)
root.insert(20)
root.insert(1)  # Insert 1 to test the new functionality
root.insert(60)
inOrderTraversal(root)
