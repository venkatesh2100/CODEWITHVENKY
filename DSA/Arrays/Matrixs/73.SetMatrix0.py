class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TODO: find the row or col which had 0's
        row = len(matrix)
        col = len(matrix[0])

        rowset = set()
        colset = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rowset.add(r)
                    colset.add(c)
        for r in range(row):
            for c in range(col):
                if r in rowset or c in colset:
                    matrix[r][c] = 0
        return matrix
