class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            nums.reverse()
            return nums
        for i in range(n-1,index,-1):
            if nums[i] > nums[index]:
                nums[i] , nums[index] = nums[index] , nums[i]
                break
        print(nums)
        nums[index+1:] = reversed(nums[index+1:])

        return nums


a = Solution()
arr = [1,2,3]
print(a.nextPermutation(arr))