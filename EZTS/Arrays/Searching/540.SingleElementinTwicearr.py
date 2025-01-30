class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # TODO: Use binary search ODD or EVEN sides

        left = 0
        right = len(nums) - 1
        # if len(nums) ==1:
        #     return nums[0]

        while left < right:
            mid = left + (right - left)//2
            # print(left , right , mid ,nums[mid])
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
