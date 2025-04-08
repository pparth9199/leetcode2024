class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        result = []

        for d in range(rows + cols - 1):
            intermediate = []
            r = rows - 1 if d < cols else rows - 1 - (d - cols + 1)
            c = d if d < cols else cols - 1

            while r >= 0 and c >= 0 and r < rows and c < cols:
                intermediate.append(matrix[r][c])
                r -= 1
                c -= 1
            if len(set(intermediate)) != 1:
                return False
        return True