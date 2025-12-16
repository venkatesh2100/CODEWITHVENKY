class Solution:
    def permute(self, s: str):
        res = []

        def backtrack(path, remain):
            if not remain:
                res.append(path)
                return

            for i in range(len(remain)):
                backtrack(
                    path + remain[i],
                    remain[:i] + remain[i+1:]
                )

        backtrack("", s)
        return res


ans = Solution()
s = "abc"
per = ans.permute(s)
print(per)
