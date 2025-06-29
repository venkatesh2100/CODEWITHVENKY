
# 2200. Find All K-Distant Indices in an Array
# nums = [3,4,9,1,3,9,5], key = 9, k = 1
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        arrI = []
        for i, val in enumerate(nums):
            if val == key:
                arrI.append(i)

        print(arrI)
        # for i in range(len(nums)):
        #     for
        arr = set()
        for index in arrI:
            lb = index
            rb = index + 1
            while lb > 0 or rb < len(nums):
                if abs(lb - index) <= k:
                    arr.add(lb)
                    lb -= 1
                if abs(rb - index) <= k:
                    arr.add(rb)
                    rb += 1
                else:
                    break
        return arr


ans = Solution()
nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1
print(ans.findKDistantIndices(nums, key, k))
