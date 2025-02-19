from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        res = []
        hashmap = {nums2[len(nums2)-1]:-1}
        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)
            
            # stack.append(num)
        # print(hashmap)
        for num in nums1:
            res.append(hashmap.get(num,-1))
        return res
