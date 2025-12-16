class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [ ]
        opera = ["*","+","/","-"]
        for tok in tokens:

            if not stack:
                stack.append(tok)

            if tok in opera:
                self.helper(opera,stack)

        return stack[-1]
    def helper(self,opera , stack):
        a = stack.pop()
        b = stack.pop()
        if opera == "*":
          return   self.stack.append(a * b)
        elif opera == "-":
           return  self.stack.append(a - b)
        elif opera == "+":
            return self.stack.append(a + b)
        else:
           return  self.stack.append( a / b)



        
