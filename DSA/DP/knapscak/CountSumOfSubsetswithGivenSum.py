# 1 1 2 3 k = 4
class Solution:
    def CountSumofSubsetswithSum(self, nums, target) -> int:

        # Tabulation Method [knapsack]
        r = len(nums)
        c = target
        dp = [[0] * (c+1) for _ in range(r+1)]

        # pre init

        for i in range(r+1):
            dp[i][0] = 1

        for i in range(1, r+1):
            for j in range(1, c+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[r][c]


ans = Solution()
arr = [1, 1, 2, 3]
res = ans.CountSumofSubsetswithSum(arr, 4)
print(res)
