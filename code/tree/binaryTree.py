from colorama import Fore, Style
class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val

    def insertval(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insertval(val)
            else:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insertval(val)
        else:
            self.val = val

    def inorderTraversal(self, root):
        res = []
        if root:
            res = res + self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

    def print_tree_christmas(self, level=0, prefix="Root: "):
        """Print the tree in a Christmas Tree-like structure."""
        # Create a visual representation of the tree
        if self is None:
            return

        # Print the current node
        print(' ' * (level * 4) + Fore.RED + prefix + str(self.val) + Style.RESET_ALL)
        # Recursively print left and right subtrees with added space
        if self.left:
            self.left.print_tree_christmas(level + 1, "/--")
        else:
            print(' ' * ((level + 1) * 4) + "/-- None")

        if self.right:
            self.right.print_tree_christmas(level + 1, "\\--")
        else:
            print(' ' * ((level + 1) * 4) + "\\-- None")


# Create a tree and insert values
root = Node(10)
root.insertval(20)
root.insertval(9)
root.insertval(30)
root.insertval(1)
root.insertval(40)
root.insertval(5)

# Print the tree in a "Christmas Tree-like" structure
print("\nChristmas Tree-like Structure:\n")
root.print_tree_christmas()

# Inorder Traversal
print("\nInorder Traversal:", root.inorderTraversal(root))
