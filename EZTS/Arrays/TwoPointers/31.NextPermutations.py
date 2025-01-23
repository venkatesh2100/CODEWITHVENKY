class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # TODO: Find the Break point and then Swap the Values upto Index Value
        index = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        # print(index)
        # HACK: If value is Greatest Number than reverse it to START
        if index == -1:
            nums.reverse()
            return nums

        # HACK: Now Swap the Index value with Larger Value
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        # HACK: Sort the Remain Part
        nums[index+1:] = sorted(nums[index+1:])

        return nums
