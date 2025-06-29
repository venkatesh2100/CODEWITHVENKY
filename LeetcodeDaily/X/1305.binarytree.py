
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        def bfs(root):
            if not root:
                return None
            q = deque([root])
            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    arr.append(curr.val)
                    root.append(curr.left)
                    root.append(curr.right)
