# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # Try to Gahter the Parent and child Relation into P hashmap.
        # and then Try to create V hmap to check whether the  val is not repeat.
        ans = []
        p = {}
        q = deque([root])
        # Normal BFs or lvl order.
        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    p[curr.left.val] = curr
                    q.append(curr.left)
                if curr.right:
                    p[curr.right.val] = curr
                    q.append(curr.right)
        # try to travese from target to all directions and check the distance satify k.
        v = {}
        q.append([target])

        while k and q:
            for _ in range(len(q)):
                curr = q.popleft()
                v[curr.val] = 1
                if curr.left and curr.left.val not in v:
                    q.append(curr.left)
                if curr.right and curr.right.val not in v:
                    q.append(curr.right)

                if p[curr] and p[curr].val not in v:
                    q.append(p[curr.val])
                k -= 1
        # the remain q values are Res
        #
        res = []
        while q:
            res.append(q.popleft())
        return res
