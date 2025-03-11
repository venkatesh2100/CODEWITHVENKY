from list Import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        idx = 0
        for i ,val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                res[stack.pop()] = val
            stack.append(i)
        for i ,val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                res[stack.pop()] = val
            stack.append(i)
        return res


