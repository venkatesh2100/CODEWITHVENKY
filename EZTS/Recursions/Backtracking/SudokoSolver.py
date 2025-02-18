class Solution:
    def solveSudoku(self, board: list[list[str]]) -> list[list[str]]:
        n = 9
        def isValid(row, col, ch):
            row, col = int(row), int(col)

            for i in range(9):

                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False

                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            return True
        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row+1, 0)

            if board[row][col] == ".":
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)

                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)
        solve(0, 0)
        return board
ans = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(ans.solveSudoku(board))