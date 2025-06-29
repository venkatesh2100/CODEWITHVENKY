class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for idx in range(len(s)-1):

            count += abs(ord(s[idx])- ord(s[idx + 1]))
        return count
