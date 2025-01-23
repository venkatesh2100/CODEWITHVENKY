

class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:

        rows = len(mat)
        cols = len(mat[0])

        rowsCount = [cols] * rows
        colsCount = [rows] * cols

        positionMap = {}
        for r in range(rows):
            for c in range(cols):
                positionMap[mat[r][c]] = (r, c)

        for idx, val in enumerate(arr):
            row, col = positionMap[val]

            rowsCount[row] -= 1
            colsCount[col] -= 1
            if rowsCount[row] == 0 or colsCount[col] == 0:
                return idx
        return -1


arr = [1, 3, 4, 2]
mat = [[2, 2], [3, 4], [3, 2], [3, 1]]
ans = Solution()
print(ans.firstCompleteIndex(arr, mat))
