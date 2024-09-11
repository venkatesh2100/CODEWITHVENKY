# Siliding window technique:
# [2, 1, 5, 1, 3, 2]
#
#


def maxsum(arr ,n):
    res=0
    max_sum=float('-inf')
    for i in range(n):
        res+=arr[i] 
    max_sum=res
    for i in range(n,len(arr)):
        res+=arr[i]-arr[i-n]
        max_sum=max(max_sum,res)


    return max_sum






nums=[10,1,5,1,3,2]

window=3

result=maxsum(nums,window)

print(max,result)
