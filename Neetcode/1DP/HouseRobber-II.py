from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        House Robber II
        - Similar to House Robber I, but the houses are arranged in a circle
        - This means the first and last houses are adjacent
        """

        def helper(arr):
            if not arr:
                return 0

            if len(arr) == 1:
                return arr[0]

            if len(arr) == 2:
                return max(arr)

            dp = [0] * (len(arr) + 1)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-2]

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))


sol = Solution()
print(sol.rob([1, 2, 3, 1]))  # Output: 3
