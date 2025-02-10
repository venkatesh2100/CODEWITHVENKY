class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = ''
        # Recursion Tree .
        def dfs(left:int ,right:int , s):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if left < n:
                dfs(left+1 ,right , s+'(')
            if right < left:
                dfs(left ,right+1,s+')')

        return dfs(0,0,s)
    
