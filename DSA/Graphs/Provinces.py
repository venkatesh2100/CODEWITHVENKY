from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not vis[j]:
                    print(vis)
                    vis[j] = True
                    dfs(j)

        vis = [False] * len(isConnected)
        graphC = 0
        for i in range(len(isConnected)):
            if not vis[i]:
                graphC += 1
                vis[i] = True
                dfs(i)

        return graphC


isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
ans = Solution()

print(ans.findCircleNum(isConnected))
