class Solution:
#   Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
    def findThePrefixCommonArray(self, A, B):
        hashMap = {}
        for i in range(len(A)):
            hashMap[A[i]]=hashMap.get(A[i],0)+1
            hashMap[B[i]]=hashMap.get(B[i],0)+1

        return hashMap


A = [1,3,2,4]
B = [3, 1, 2, 4]
ans = Solution.findThePrefixCommonArray(A,B)
print(ans)
