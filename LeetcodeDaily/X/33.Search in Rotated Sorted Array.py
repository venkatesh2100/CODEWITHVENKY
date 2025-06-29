
def findPeakElement(nums) -> int:
  ##? compare the mid element with surrondings... if mid less then shift left else shift right
  l=0
  r=len(nums)-1
  while l<r:
    mid=l+(r-l)//2
    print(mid,l,r)
    if nums[mid]>nums[mid+1]:
      r=mid
    else:
      l=mid+1
  return l


print(findPeakElement([1,2,1,3,4,5,6]))