from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        subBoard = [set() for _ in range(9)]
        emptyCells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    emptyCells.append((r,c))
                else:
                    val = board[r][c]
                    rowset[r].add(val)
                    colset[c].add(val)
                    subBoard[(r//3)*3 +(c//3)].add(val)


        def solve(index):
            if index == len(emptyCells):
                return True

            row ,col = emptyCells[index]
            subBoxValue = (row//3)* 3 + (col//3)

            for num in map(str,range(1,10)):
                if num not in rowset[row] and num not in colset[col] and num not in subBoard[subBoxValue]:
                    board[row][col] = num
                    rowset[row].add(num)
                    colset[col].add(num)
                    subBoard[subBoxValue].add(num)

                    if solve(index+1):
                        return True

                    board[row][col] = "."
                    rowset[row].remove(num)
                    colset[col].remove(num)
                    subBoard[subBoxValue].remove(num)
            return False
        solve(0)
