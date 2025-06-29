class solution:
    def threesum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        num = list(dict.fromkeys(nums))
        n = len(num)
        arr = []
        for i in range(n):
            l = i + 1
            r = n - 1
            sum = nums[l] + nums[r]+nums[i]
            if sum == 0:
                arr.append([num[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif sum > 0:
                r -= 1
            else:
                l += 1
        return arr

nums = [-2, 1, -2, 4, 3]
sol=solution()
threesu=sol.threesum(nums)
print(threesu)


class solution:
    def threesum(self,nums:list[int]->listl[list[int]]):

        nums.sort()
        n=len(nums)
        arr=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue

            l,r=i+1,n-1

            sum=nums[i]+nums[l]+nums[r]
            if sum==0:
                arr.append(nums[i],nums[l],nums[r])

                l+=1
                r-=1

                #duplicates skips
            elif sum>0:
                l+=1
            else:
                r-=1
     return arr[]
