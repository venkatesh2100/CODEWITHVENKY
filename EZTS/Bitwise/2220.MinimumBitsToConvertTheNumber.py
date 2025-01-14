from collections import deque
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binVal1 = bin(start)[2:]
        binVal2 = bin(goal)[2:]
        # dq = []
        # lenbinVal2 = len(binVal2)
        # while lenbinVal2!=len(binVal1):
        #   dq.append(0)
        #   lenbinVal2+=1
        while len(binVal1) < len(binVal2):
            binVal1 = '0' + binVal1
        while len(binVal2) < len(binVal1):
            binVal2 = '0' + binVal2
        # for binary in binVal2:
        #   dq.append(binary)

        count = 0
        # binVal2 = [''.join(str(val) for val in dq)]
        # print(binVal1,binVal2)
        # print(dq[1])
        for i in range(len(binVal1)):
            if binVal1[i]!=binVal2[i]:
                count+=1
        return count

ans = Solution()
print(ans.minBitFlips(10,7))