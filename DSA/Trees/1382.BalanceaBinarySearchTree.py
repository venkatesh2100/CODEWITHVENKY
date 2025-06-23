# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        arr = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        
        def build_tree(left,right):
            if left > right:
                return None
            
            mid =  left + (right - left)//2 
            node = TreeNode(arr[mid])

            node.left = build_tree(left , mid - 1)
            node.right = build_tree(mid+1, right)

            return node 
        return  build_tree(0,len(arr)- 1)
        
