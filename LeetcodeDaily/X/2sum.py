class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap={}
        n=len(nums)


        for i in range(n):
            hashMap[nums[i]]=i

        for i in range(n):
            comp=target-nums[i]
            if comp in hashMap and hashMap[comp]!=i:
                return [i,hashMap[comp]]

        return []
