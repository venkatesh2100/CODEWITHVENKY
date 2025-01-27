# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # TODO: BFS the Entire Tree and then Find the val in the Range and Add it
        sumi: int = 0
        self.bfs(root, low, high, sumi)

    def bfs(self, root, low, high, sumi):
        if not root:
            return None

        if low <= root.val <= high:
            sumi += root.val
        if root.val > low:
            return self.bfs(root.left, low, high, sumi)
        if root.val < high:
            return self.bfs(root.right, low, high, sumi)
        return sumi
