class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        subtree = []
        # nums = [1  , 2, 3, 4 , 5 ,6 , 7 , 8 ,9]
        #TODO: RT count the sum of the subtree and then pop accroding to the condtions. Recursions Trees.
        def helper(i:int ,curr_sum:int):
            if i > 10 or curr_sum > n:
                return 
            # print(subtree[:])
            if curr_sum == n and len(subtree)==k and subtree[:] not in res:
                res.append(subtree[:])
            subtree.append(i)
            helper(i+1,curr_sum + i)
            subtree.pop()
            helper(i+1 ,curr_sum)
        helper(1,0)
        return res
