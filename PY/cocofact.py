N = int(input())
arr = list(map(int,input().split(',')))

j = 0 
for i in range(N):
    temp = 0
    if arr[i] != 0:
        temp = arr[i] 
        arr[i] = arr[j]
        arr[j] = temp
        j+=1
print(arr)
# eof





# res = []
# count = 0
# for c in arr:
#     if c != 0:
#         res.append(c)
#     else:
#         count+=1
#     
# for i in range(count):
#     res.append(0)
#
# print(res)
