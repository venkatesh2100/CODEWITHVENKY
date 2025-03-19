''' 4 1 1 1 2 3 5'''
### Variable Size Sliding window.

def SubarrayLargest(arr, k):
  l = 0
  r = 0
  count = 0
  res = 0


  while r < len(arr):
    count+=arr[r]
    if count == k:
      res = max(res,r-l+1)
    while count > k:
      count-=arr[l]
      l+=1
    r+=1
  return res


arr = [4,1,1,1,2,3,4]
print(SubarrayLargest(arr,5))