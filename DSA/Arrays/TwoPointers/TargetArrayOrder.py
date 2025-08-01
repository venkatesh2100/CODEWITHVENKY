# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#
#     Initially target array is empty.
#     From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#     Repeat the previous step until there are no elements to read in nums and index.
#
# Return the target array.
#
# It is guaranteed that the insertion operations will be valid.
#
#
#
# Example 1:
#
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
import enum


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        res = [[] for _ in range(len(nums))]

        for i, x in enumerate(index):
            res[x].append(nums[i])
        # print(res)
        ans = []
        for x in res:
            val = sorted(x, reverse=True)
            for v in val:
                ans.append(v)
        return ans
