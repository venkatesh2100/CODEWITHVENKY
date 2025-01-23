from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # HACK: mat = [[0,0,0],[0,1,0],[0,0,0]]
        #
        row = len(mat)
        col = len(mat[0])

    # Distance Matrix which contains NEW rows and colums
        distance = [[float('inf')] * col for i in range(row)]
        que = deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    distance[r][c] = 0
                    que.append([r, c])

    # Now checking the +N S E W for the Distance

        dis = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while que:
            r, c = que.popleft()

            for dr, dc in dis:
                nr, nc = dr + r, dc + c
                if 0 <= nr < row and 0 <=nc < col:
                    if distance[nr][nc] > distance[r][c]+1:
                        distance[nr][nc] = distance[r][c]+1
                        que.append([nr, nc])
        return distance


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ans = Solution()
print(ans.updateMatrix(mat))
