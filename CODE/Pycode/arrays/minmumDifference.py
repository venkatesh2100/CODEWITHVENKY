
class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        count=0

        if k==0:
            return 0
        diff=0

        minval=float('inf')
        for i in range(len(nums)-k+1):
            diff=nums[i+k-1] -nums[i]

            if diff < minval:
                 minval=diff
                 count=1
            elif diff==minval:
                count+=1

        return count


[1 ,4, 7, 9]


