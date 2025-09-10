

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            - Here we can Start either 0 or 1 index and find Min(0-x , 1-x) costs.
        """
        def dfs(i, res):
            if i >= n:
                return 0
 
            res = min(res+cost[i], cost[i+1])
            dfs(i+1)
            dfs(i+2)
            return res
        return min(dfs(0), dfs(1))


sol = Solution()
ans = sol.minCostClimbingStairs([10, 15, 20])
print(ans)
