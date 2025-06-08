# updated new neovim configs HHAHAHAHHAH.
# Tree.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def Tree(root):
        if not root:
            return False 
        
        lh = Tree(root.left)
        rh = Tree(root.right)
        
        return lh  + rh
