from collections  import Counter
class Solution:
    def minFlips(self, s: str) -> int:

        fq = Counter(s)
        if len(s) < 3:
            return 0
        # print(fq)
        if  not fq.get('0') or not fq.get('1'):
            return 0
        # print(fq['1'])
        return fq.get('1',0) - 1


ans = Solution()
s = '0011'
res = ans.minFlips(s)
print('Result', res)
