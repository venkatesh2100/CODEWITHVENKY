class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        # TODO:: GRID AUTO Leetcode
        firstRow = sum(grid[0])
        secondRow = 0
        minSum = float('inf')

        for idx in range(len(grid[0])):
            firstRow -= grid[0][idx]

            minSum = min(minSum, max(firstRow, secondRow))
            secondRow += grid[1][idx]
        return int(minSum)


ans = Solution()
grid = [[2, 5, 4], [1, 5, 1]]
print(ans.gridGame(grid))
