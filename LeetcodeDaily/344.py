# 344. Reverse String
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        l = 0
        r = N - 1
        while l < r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            l += 1
            r -= 1
        print(s)


s = ["h", "e", "l", "l", "o"]
ans = Solution()

print(ans.reverseString(s))
