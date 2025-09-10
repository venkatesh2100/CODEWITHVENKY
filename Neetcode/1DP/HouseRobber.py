from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - We are given a list of non-negative integers representing the amount of money of each house
        - We are to determine the maximum amount of money we can rob tonight without alerting the police
        - Adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night
        - Example 1:
            Input: nums = [1,2,3,1]
            Output: 4
            Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        """
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Creating DP Cache 1D table

        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        print(dp)
        return dp[n - 1]


sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 4
