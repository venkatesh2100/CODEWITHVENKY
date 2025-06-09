class Solution:
#   Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        res = [0]*len(A)
        hashMap = {}
        # count = 0
        for i in range(len(A)):
            hashMap[A[i]]=hashMap.get(A[i],0)+1
            hashMap[B[i]]=hashMap.get(B[i],0)+1

            # if hashMap.get(A[i])>=2 or hashMap.get(B[i])>=2:
            #     count+=1
            count = 0
            for key,val in hashMap.items():
                if val>=2:
                    count+=1
            res[i]=count
            # print(hashMap)
            # print(f"hashMap",hashMap ,"count",count ,"RES",res)

        return res


A = [1,3,2,4]
B = [3, 1, 2, 4]
ans = Solution()
print(ans.findThePrefixCommonArray(A,B))
