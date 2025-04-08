class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        result = []

        for d in range(rows + cols - 1):
            intermediate = []

            r = 0 if d < cols else d - cols + 1
            c = d if d < cols else cols - 1

            while r < rows and c >= 0:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result
            

        

