class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hmap = {"}":"{" , "]":"[" , ")":"("}
        for w in s:
            if not stack:
                stack.append(w)

            if stack[-1] == hmap.get(w):
                stack.pop()
            else:
                stack.append(w)
        return True if not stack else False 
        
        
