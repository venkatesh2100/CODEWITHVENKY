class Solution:
    def climbStairs(self, n: int) -> int:
        """
        - We can Jump Either 1 or 2 steps forward - reach the End point
        - if N = 3 1 + 1 + 1 or 1 + 2 or 2 + 1
         1. using Bottom up approach
        """
        # USing DP
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    # using then


sol = Solution()
ans = sol.climbStairs(3)
print(ans)
