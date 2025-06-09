
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        top = 0
        bottom = n - 1
        # TODO: NOW change the Position Swap of ROWS UP and Bottom
        while top < bottom:
            for col in range(n):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1
        # HACK: Now Invert the Array Easy
        for row in range(n):
            for col in range(row+1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        return matrix
