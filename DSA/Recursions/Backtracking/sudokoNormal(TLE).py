class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #TODO: Iterate over the board if null then try insert a value and check isvalid if not backtrack.

        def solver(board):

            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for val in range(1,10):
                            if isvalid(r,c,str(val)):

                                board[r][c]= str(val)

                                if solver(board):
                                    return True
                                else:
                                    board[r][c] ="."
                    return False
            return True
        
        def isvalid(row,col,val):
            for i in range(9):
                if board[row][i] == val:
                    return False
                elif board[i][col] == val:
                    return False
                elif board[3*(row//3)+i//3][3*(col//3)+i%3] == val:
                    return False
            return True
        solver(board)
