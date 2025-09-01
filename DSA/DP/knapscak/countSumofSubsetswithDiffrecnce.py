

class Solution:
    def DiffDpCount(self, nums, diff) -> int:

        r = len(nums)
        target = (diff + sum(nums))//2

        dp = [[0] * (target + 1) for _ in range(r+1)]

        for i in range(r+1):
            dp[i][0] = 1

        for i in range(1, r+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[r][target]


ans = Solution()
nums = [1, 1, 2, 3]
res = ans.DiffDpCount(nums, 1)
print(res)
