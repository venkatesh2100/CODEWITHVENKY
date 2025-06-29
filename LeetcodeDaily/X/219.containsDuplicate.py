class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:


        HasMap={}

        for i,num in enumerate(nums):
            if num in HasMap and i - HasMap[num]<=k:
                return True
        HasMap[num]=i

        return False
