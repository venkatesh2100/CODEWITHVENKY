from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            midA = left + (right - left) // 2
            midB = (m + n + 1) // 2 - midA

            maxLeftA = float('-inf') if midA == 0 else nums1[midA - 1]
            minRightA = float('inf') if midA == m else nums1[midA]
            maxLeftB = float('-inf') if midB == 0 else nums2[midB - 1]
            minRightB = float('inf') if midB == n else nums2[midB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = midA - 1
            else:
                left = midA + 1
