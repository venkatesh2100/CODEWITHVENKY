class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -2 -1 3 4 5 
        nums.sort()
        num=list(dict.fromkeys(nums))
       size=size(num)
        arr=[][]
        for i in range(size):
            l=i+1
            r=size-1
            sum=nums[l]+nums[r]
            if(sum+num[i]==0):
                arr.append(i,l,r)
            if(sum>num[i]):
                r--
            elif:
                l++

nums=[-2,1,-2,4,3]
print(threeSum(nums))

