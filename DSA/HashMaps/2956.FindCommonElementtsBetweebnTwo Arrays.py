from typing import Counter


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashmap1 = Counter(nums1)
        hashmap2 = Counter(nums2)
        seen  = set()
        r = 0 
        l = 0
        for key , items in hashmap1.items():
            if key in hashmap2:
                seen.add(key)
                l+= hashmap1[key]
        for key , items in hashmap2.items():
            if  key in seen:
                r+= hashmap2[key]
            elif key in hashmap1:
                r+= hashmap2[key]
        return [l,r]
