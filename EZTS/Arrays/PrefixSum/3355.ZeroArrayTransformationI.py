'''You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.
'''

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        # freq = defaultdict(int)
        sweep = [0] * (N + 1)
        for l , r in queries:
            sweep[l]+=1
            sweep[r+1]-=1
        # print(sweep)
        curr = 0
        for idx in range(len(nums)):
            # print(nums[idx],freq[idx])
            curr+=sweep[idx]
            if nums[idx]!=0 and curr < nums[idx]:
                return False
        return True

