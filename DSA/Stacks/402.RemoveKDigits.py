class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        

        stack = []
        sz = len(num)

        for w in num:
            while k > 0 and stack and stack[-1] > w:
                stack.pop()
                k-=1
            if not stack and w=='0':
                continue
            stack.append(w)
        while  stack and k:
            stack.pop()
            k-=1

        return ''.join(stack) if stack else "0"

