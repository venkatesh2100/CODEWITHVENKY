class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        abc = 'a' 'b' 'c'
        """

        n = len(s)
        res = 0
        a = 0
        c = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[i] == s[r]:
                c += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[i] == s[r]:
                a += 1
                l -= 1
                r += 1
            res = max(a, c)
        return res
