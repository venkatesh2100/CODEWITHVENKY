
# nums = [1,2,3,1]


class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        memo = [-1] * N
        result = -1

        def dp(index):
            if index == -1:
                return 0
            if index == 0:
                return nums[0]
            if memo[index] != -1:
                return memo[index]
            pick = nums[index] + dp(index - 2)
            not_pick = dp(index - 1)
            result = max(pick, not_pick)
            memo[index] = result
            return result

        return dp(N-1)
