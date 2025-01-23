# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

      currSumSum = 0
      def dfs(node):

          if not node:
              return
          nonlocal currSumSum
          dfs(node.right)
          temp = node.val
          node.val += currSum
          currSum += temp
          dfs(node.left)
      dfs(root)
      return root