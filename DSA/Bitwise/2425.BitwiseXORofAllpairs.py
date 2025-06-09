class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:

        # memo = []
        # # i = 0
        """
        This Approach Eliminate the completed Computaions which Every Element in the  one vs Two
        """
        xor1 = 0
        xor2 = 0
        for one in nums1:
            xor1 ^= one
        for two in nums2:
            xor2 ^= two
        res = 0
        if len(nums1) % 2 != 0:
            res ^= xor2
        if len(nums2) % 2 != 0:
            res ^= xor1
        return res

        # return xor1 * xor2
        # for one in nums1:
        #     for two in nums2:
        #         # newArray.append( one ^ two )
        #         arrayValue = one ^ two
        #         res = res ^ arrayValue
        # return res
        # # print(newArray)
        """
        Iterate through the Array - MEMLE
        i = 1
        res = newArray[0]
        while i < len(newArray):
            res = res ^ newArray[i]
            i +=1
        return res
        """
ans = Solution()
print(ans.xorAllNums([2,1,3] , [10,2,5,0]))